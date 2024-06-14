from django.urls import path
from .views import (
    SupplierCreateView, SupplierUpdateView, SupplierDeleteView, 
    SupplierListView, SupplierDetailView, ReadSupplierByID
)

urlpatterns = [
    path('suppliers/', SupplierListView.as_view(), name='supplier-list'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier-create'),
    path('suppliers/<uuid:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('suppliers/<uuid:pk>/update/', SupplierUpdateView.as_view(), name='supplier-update'),
    path('suppliers/<uuid:pk>/delete/', SupplierDeleteView.as_view(), name='supplier-delete'),
    path('suppliers/read/<uuid:pk>/', ReadSupplierByID.as_view(), name='supplier-read-by-id'),
]
