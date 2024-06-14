from decimal import Decimal
from django.test import TestCase
from .models import Item
from .serializers import ItemSerializer
from categories.models import Category
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ItemModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            name="Laptop",
            price="999.99",
            description="High-performance laptop"
        )

    def test_item_creation(self):
        self.assertIsInstance(self.item, Item)
        self.assertEqual(self.item.__str__(), self.item.name)
        self.assertEqual(self.item.name, "Laptop")
        self.assertEqual(self.item.price, "999.99")
        self.assertEqual(self.item.description, "High-performance laptop")

    def test_item_uuid(self):
        self.assertIsNotNone(self.item.id)

    def test_item_timestamps(self):
        self.assertIsNotNone(self.item.created_at)
        self.assertIsNotNone(self.item.updated_at)


class ItemSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Electronics",
            description="Electronic items"
        )
        self.item_data = {
            "name": "Laptop",
            "price": "999.99",
            "description": "High-performance laptop",
            "category": str(self.category.id)
        }
        self.item = Item.objects.create(**self.item_data)
        self.serializer = ItemSerializer(instance=self.item)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(
            ['id', 'name', 'price', 'description', 'category', 'created_at', 'updated_at']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.item_data['name'])

    def test_price_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['price'], self.item_data['price'])

    def test_description_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['description'], self.item_data['description'])


class ItemViewTests(APITestCase):
    fixtures = ['categories/fixtures/initial_data.json',
                'items/fixtures/items.json']

    def test_create_item(self):
        # Create a category
        category = Category.objects.create(
            name="Electronics",
            description="Electronic items"
        )
        url = reverse('item-create')
        data = {
            "name": "Tablet",
            "price": "499.99",
            "description": "A new tablet",
            "category": str(category.id)
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 3)
        self.assertEqual(Item.objects.get(
            name="Tablet").description, "A new tablet")

    def test_list_items(self):
        url = reverse('item-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure response data contains 'results'
        self.assertIn('results', response.data)

        # Ensure 'results' is a list
        self.assertIsInstance(response.data['results'], list)

        # Check the length of the list
        expected_length = Item.objects.count()
        self.assertEqual(len(response.data['results']), expected_length)

        # Validate the actual content
        received_names = {item['name'] for item in response.data['results']}
        expected_names = {item.name for item in Item.objects.all()}
        self.assertEqual(received_names, expected_names)

    def test_retrieve_item(self):
        item = Item.objects.get(name="Laptop")
        url = reverse('item-detail', kwargs={'pk': item.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Laptop")

    def test_update_item(self):
        item = Item.objects.get(name="Laptop")
        url = reverse('item-update', kwargs={'pk': item.id})
        data = {"name": "Updated Laptop",
                "price": "1099.99",
                "description": "Updated description",
                "category": str(item.category.id)}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item.refresh_from_db()
        self.assertEqual(item.name, "Updated Laptop")
        self.assertEqual(item.price, Decimal("1099.99"))
        self.assertEqual(item.description, "Updated description")

    def test_delete_item(self):
        item = Item.objects.get(name="Laptop")
        url = reverse('item-delete', kwargs={'pk': item.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        item.refresh_from_db()
        self.assertEqual(Item.objects.count(), 2)
