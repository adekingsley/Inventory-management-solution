from django.urls import path
from .views import (
    InStockStockListView, InventoryDetailView, InventoryListView, OutOfStockStockListView, StockCreateView, StockUpdateView, StockDeleteView,
    StockListView, StockDetailView, ReadStockByID
)

urlpatterns = [
    path('stocks/', StockListView.as_view(), name='stock-list'),
    #     path('stocks/create/', StockCreateView.as_view(), name='stock-create'),
    path('stocks/<uuid:pk>/', StockDetailView.as_view(), name='stock-detail'),
    path('stocks/<uuid:pk>/update/',
         StockUpdateView.as_view(), name='stock-update'),
    path('stocks/<uuid:pk>/delete/',
         StockDeleteView.as_view(), name='stock-delete'),
    path('stocks/read/<uuid:pk>/', ReadStockByID.as_view(), name='stock-read-by-id'),

    # Inventory URLs
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/<uuid:pk>/', InventoryDetailView.as_view(),
         name='inventory-detail'),
    path('stocks/in_stock/', InStockStockListView.as_view(),
         name='in_stock_stocks'),
    path('stocks/out_of_stock/', OutOfStockStockListView.as_view(),
         name='out_of_stock_stocks'),
]
