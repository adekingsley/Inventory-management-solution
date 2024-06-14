from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'description',
                  'category', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        """
        Check that the item name is unique within the same category.
        """
        if Item.objects.filter(name=data['name'], category=data['category']).exists():
            raise serializers.ValidationError(
                "An item with this name already exists in the selected category.")
        return data
