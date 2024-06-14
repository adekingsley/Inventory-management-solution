from django.urls import path
from .views import (
    ItemCreateView, ItemUpdateView, ItemDeleteView, 
    ItemListView, ItemDetailView, ReadItemByID
)

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/create/', ItemCreateView.as_view(), name='item-create'),
    path('items/<uuid:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/<uuid:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('items/<uuid:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('items/read/<uuid:pk>/', ReadItemByID.as_view(), name='item-read-by-id'),
]
