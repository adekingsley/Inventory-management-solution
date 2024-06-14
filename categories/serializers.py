from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_name(self, value):
        """
        Check that the category name is unique.
        A. Check for uniqueness excluding the current instance
        B. Check for uniqueness during creation

        """
        if self.instance:
            if Category.objects.filter(name=value).exclude(pk=self.instance.pk).exists():
                raise serializers.ValidationError(
                    "A category with this name already exists.")
        else:
            if Category.objects.filter(name=value).exists():
                raise serializers.ValidationError(
                    "A category with this name already exists.")
        return value
