from django.urls import path
from .views import (
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView, 
    CategoryListView, CategoryDetailView, ReadCategoryByID
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<uuid:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<uuid:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<uuid:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('categories/read/<uuid:pk>/', ReadCategoryByID.as_view(), name='category-read-by-id'),
]
