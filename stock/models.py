from django.db import models
import uuid
from django.dispatch import receiver
from django.db.models.signals import pre_save


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Stock(TimeStampModel):
    OUT_OF_STOCK = 'out_of_stock'
    IN_STOCK = 'in_stock'
    OVERSTOCK = 'overstock'

    STOCK_STATUS_CHOICES = [
        (OUT_OF_STOCK, 'Out of Stock'),
        (IN_STOCK, 'In Stock'),
        (OVERSTOCK, 'Overstock'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(
        "items.Item", on_delete=models.CASCADE, related_name='stock')
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STOCK_STATUS_CHOICES,
        default=IN_STOCK
    )

    def __str__(self):
        return f"Stock of {self.item.name}: {self.quantity}"

    class Meta:
        indexes = [
            models.Index(fields=['item']),
        ]
        ordering = ['item']


@receiver(pre_save, sender=Stock)
def update_stock_status(sender, instance, **kwargs):
    if instance.quantity < 10:
        instance.status = Stock.OUT_OF_STOCK
    elif instance.quantity > 50:
        instance.status = Stock.OVERSTOCK
    else:
        instance.status = Stock.IN_STOCK


class Inventory(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(
        "items.Item", on_delete=models.CASCADE, related_name='inventory')
    purchase = models.ForeignKey("transactions.Purchase", null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name='inventory_purchases')
    sale = models.ForeignKey("transactions.Sale", null=True, blank=True,
                             on_delete=models.SET_NULL, related_name='inventory_sales')
    purchase_quantity = models.FloatField(null=True, blank=True)
    sale_quantity = models.FloatField(null=True, blank=True)
    total_balance_quantity = models.FloatField()

    def __str__(self):
        return f"Inventory for {self.item.name}"

    class Meta:
        indexes = [
            models.Index(fields=['item']),
        ]
        ordering = ['-created_at']
