from django.db import models
import uuid
from django.forms import ValidationError
from django.utils.text import slugify

from stock.models import Stock


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Item(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, blank=False)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="items", db_index=True, null=True, blank=True)
    image = models.ImageField(upload_to='item_images/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Item.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

        # Ensure Stock is created when Item is created
        Stock.objects.get_or_create(item=self, defaults={'quantity': 0})

    def clean(self):
        if self.price < 0:
            raise ValidationError("Price cannot be negative")

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['price']),
        ]
        ordering = ['name']
        # Added unique_together constraint
        unique_together = [['name', 'category']]

    @property
    def short_description(self):
        return self.description[:50]
