# Generated by Django 5.0.6 on 2024-06-13 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_sale_inventory_sale'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]