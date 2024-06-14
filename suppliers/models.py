from django.db import models
import uuid


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Supplier(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, blank=False)
    contact_name = models.CharField(max_length=100, blank=False)
    contact_email = models.EmailField(max_length=254, blank=False)
    contact_phone = models.CharField(max_length=20, blank=False)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['contact_email']),
        ]
        ordering = ['name']
