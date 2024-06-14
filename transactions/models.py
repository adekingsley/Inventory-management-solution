from django.db import models
import uuid
from decimal import Decimal
from django.db.models.signals import pre_save

from django.dispatch import receiver
from stock.models import Inventory, Stock


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Purchase(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(
        "items.Item", on_delete=models.CASCADE, related_name='purchases')
    supplier = models.ForeignKey(
        "suppliers.Supplier", on_delete=models.CASCADE, related_name='purchases')
    quantity = models.FloatField()
    price = models.FloatField()
    total_amount = models.FloatField(editable=False, default=0)

    def save(self, *args, **kwargs):
        self.total_amount = self.quantity * self.price

        # Determine if this is an update or a new purchase
        if self.pk:
            try:
                existing_purchase = Purchase.objects.get(pk=self.pk)
                quantity_difference = self.quantity - existing_purchase.quantity
            except Purchase.DoesNotExist:
                quantity_difference = self.quantity
        else:
            # If this is a new purchase, the quantity difference is the purchase quantity
            quantity_difference = self.quantity

        super(Purchase, self).save(*args, **kwargs)

        # Update inventory effect related to purchase
        inventory = Inventory.objects.filter(
            item=self.item
        ).order_by('-id').first()
        if inventory:
            total_balance = inventory.total_balance_quantity + quantity_difference
        else:
            total_balance = self.quantity

        # Insert in inventory
        Inventory.objects.create(
            item=self.item,
            purchase=self,
            sale=None,
            purchase_quantity=self.quantity,
            sale_quantity=None,
            total_balance_quantity=total_balance
        )

        # Update stock quantity
        stock, created = Stock.objects.get_or_create(item=self.item)
        stock.quantity += quantity_difference
        stock.save()

    def delete(self, *args, **kwargs):
        # Adjust stock quantity before deleting the purchase
        stock = Stock.objects.get(item=self.item)
        stock.quantity -= self.quantity
        stock.save()

        super(Purchase, self).delete(*args, **kwargs)

    def __str__(self):
        return f"Purchase of {self.quantity} {self.item.name} from {self.supplier.name}"

    class Meta:
        indexes = [
            models.Index(fields=['item']),
            models.Index(fields=['supplier']),
            models.Index(fields=['created_at']),
        ]
        ordering = ['-created_at']
        verbose_name_plural = 'Purchases'


@receiver(pre_save, sender=Purchase)
def update_stock(sender, instance, **kwargs):
    quantity_difference = instance.quantity

    # Update inventory effect related to purchase
    inventory = Inventory.objects.filter(
        item=instance.item
    ).order_by('-id').first()
    if inventory:
        total_balance = inventory.total_balance_quantity + quantity_difference
    else:
        total_balance = instance.quantity

    # Insert in inventory
    Inventory.objects.create(
        item=instance.item,
        purchase=instance,
        sale=None,
        purchase_quantity=instance.quantity,
        sale_quantity=None,
        total_balance_quantity=total_balance
    )

    # Update stock quantity
    stock, created = Stock.objects.get_or_create(item=instance.item)
    stock.quantity += quantity_difference
    stock.save()


class Sale(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(
        "items.Item", on_delete=models.CASCADE, related_name='sales')
    quantity = models.FloatField()
    total_amount = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        item_price = self.item.price  # Fetch the item's price
        self.total_amount = float(self.quantity) * float(item_price)

        # Determine if this is an update or a new sale
        if self.pk:
            # Fetch the existing sale from the database
            try:
                existing_sale = Sale.objects.get(pk=self.pk)
                # Calculate the difference in quantity
                quantity_difference = existing_sale.quantity - self.quantity
            except Sale.DoesNotExist:
                quantity_difference = -self.quantity
        else:
            # If this is a new sale, the quantity difference is negative the sale quantity
            quantity_difference = -self.quantity

        super(Sale, self).save(*args, **kwargs)

        # Update inventory effect related to sale
        inventory = Inventory.objects.filter(
            item=self.item
        ).order_by('-created_at').first()

        if inventory:
            total_balance = inventory.total_balance_quantity + quantity_difference
        else:
            total_balance = -self.quantity

        # Insert in inventory
        Inventory.objects.create(
            item=self.item,
            purchase=None,
            sale=self,
            purchase_quantity=None,
            sale_quantity=self.quantity,
            total_balance_quantity=total_balance
        )

        # Update stock quantity
        stock, created = Stock.objects.get_or_create(item=self.item)
        stock.quantity -= self.quantity
        stock.save()

    def delete(self, *args, **kwargs):
        # Adjust stock quantity before deleting the sale
        stock = Stock.objects.get(item=self.item)
        stock.quantity += self.quantity
        stock.save()

        super(Sale, self).delete(*args, **kwargs)
