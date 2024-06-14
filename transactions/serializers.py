from rest_framework import serializers
from .models import Purchase, Sale


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'item', 'supplier', 'quantity',
                  'price', 'total_amount', 'created_at']
        read_only_fields = ['id', 'total_amount', 'created_at']


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'item', 'quantity',
                  'total_amount', 'created_at']
        read_only_fields = ['id', 'total_amount', 'created_at']
