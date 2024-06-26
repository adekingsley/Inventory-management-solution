# Generated by Django 5.0.6 on 2024-06-13 14:57

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_item_unique_together'),
        ('stock', '0001_initial'),
        ('transactions', '0003_delete_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('purchase_quantity', models.FloatField(blank=True, null=True)),
                ('sale_quantity', models.FloatField(blank=True, null=True)),
                ('total_balance_quantity', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='items.item')),
                ('purchase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inventory_purchases', to='transactions.purchase')),
                ('sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inventory_sales', to='transactions.sale')),
            ],
            options={
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['item'], name='stock_inven_item_id_782a02_idx')],
            },
        ),
    ]
