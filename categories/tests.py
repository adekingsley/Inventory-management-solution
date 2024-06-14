from categories.models import Category
from django.test import TestCase
from .models import Category
import uuid
from .serializers import CategorySerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Electronics",
            description="Electronic items"
        )

    def test_category_creation(self):
        self.assertIsInstance(self.category, Category)
        self.assertEqual(self.category.__str__(), self.category.name)
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.description, "Electronic items")

    def test_category_uuid(self):
        self.assertIsInstance(self.category.id, uuid.UUID)

    def test_category_timestamps(self):
        self.assertIsNotNone(self.category.created_at)
        self.assertIsNotNone(self.category.updated_at)


class CategorySerializerTest(TestCase):
    def setUp(self):
        self.category_data = {
            "name": "Electronics",
            "description": "Electronic items"
        }
        self.category = Category.objects.create(**self.category_data)
        self.serializer = CategorySerializer(instance=self.category)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(
            ['id', 'name', 'description', 'created_at', 'updated_at']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.category_data['name'])

    def test_description_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['description'],
                         self.category_data['description'])


class CategoryViewTests(APITestCase):
    fixtures = ['initial_data.json']

    def test_create_category(self):
        url = reverse('category-create')
        data = {"name": "Clothing", "description": "Apparel items"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(Category.objects.get(
            name="Clothing").description, "Apparel items")

    def test_list_categories(self):
        url = reverse('category-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure response data contains 'results'
        self.assertIn('results', response.data)

        # Ensure 'results' is a list
        self.assertIsInstance(response.data['results'], list)

        # Check the length of the list
        self.assertEqual(len(response.data['results']), 1)

        # Validate the actual content
        expected_names = {"Electronics"}
        received_names = set([category['name']
                             for category in response.data['results']])
        self.assertEqual(received_names, expected_names)

    def test_retrieve_category(self):
        category = Category.objects.get(name="Electronics")
        url = reverse('category-detail', kwargs={'pk': category.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Electronics")

    def test_update_category(self):
        category = Category.objects.get(name="Electronics")
        url = reverse('category-update', kwargs={'pk': category.id})
        data = {"name": "Updated Electronics",
                "description": "Updated description"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category.refresh_from_db()
        self.assertEqual(category.name, "Updated Electronics")
        self.assertEqual(category.description, "Updated description")

    def test_delete_category(self):
        category = Category.objects.get(name="Electronics")
        url = reverse('category-delete', kwargs={'pk': category.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)
