# Generated by Django 5.0.6 on 2024-06-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
