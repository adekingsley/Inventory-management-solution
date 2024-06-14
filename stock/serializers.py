from rest_framework import serializers
from .models import Inventory, Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'item', 'quantity', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'item', 'purchase', 'sale', 'purchase_quantity',
                  'sale_quantity', 'total_balance_quantity', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
