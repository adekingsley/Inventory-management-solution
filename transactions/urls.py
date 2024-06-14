from django.urls import path
from .views import (
    PurchaseCreateView, PurchaseUpdateView, PurchaseDeleteView,
    PurchaseListView, PurchaseDetailView, ReadPurchaseByID, ReadSalesByID, SalesCreateView, SalesDeleteView, SalesDetailView, SalesListView, SalesUpdateView, delete_all_sales,
)

urlpatterns = [
    # Purchase URLs
    path('purchases/', PurchaseListView.as_view(), name='purchase-list'),
    path('purchases/create/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('purchases/<uuid:pk>/', PurchaseDetailView.as_view(),
         name='purchase-detail'),
    path('purchases/<uuid:pk>/update/',
         PurchaseUpdateView.as_view(), name='purchase-update'),
    path('purchases/<uuid:pk>/delete/',
         PurchaseDeleteView.as_view(), name='purchase-delete'),
    path('purchases/read/<uuid:pk>/',
         ReadPurchaseByID.as_view(), name='purchase-read-by-id'),

    # Sales URL

    path('sales/', SalesListView.as_view(), name='sale-list'),
    path('sales/create/', SalesCreateView.as_view(), name='sale-create'),
    path('sales/<uuid:pk>/', SalesDetailView.as_view(),
         name='purchase-detail'),
    path('sales/<uuid:pk>/update/',
         SalesUpdateView.as_view(), name='sale-update'),
    path('sales/<uuid:pk>/delete/',
         SalesDeleteView.as_view(), name='sale-delete'),
    path('sales/read/<uuid:pk>/',
         ReadSalesByID.as_view(), name='sale-read-by-id'),
    path('delete-sale/', delete_all_sales, name='delete_sale_at_index_1'),

]
