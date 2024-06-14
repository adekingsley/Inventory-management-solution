from rest_framework import generics
from .models import Inventory, Stock
from .serializers import InventorySerializer, StockSerializer


class StockCreateView(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockUpdateView(generics.UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockDeleteView(generics.DestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockDetailView(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class ReadStockByID(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = "pk"

# Inventory Views


class InventoryListView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDetailView(generics.RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


# Search Stocks Views
class InStockStockListView(generics.ListAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        return Stock.objects.filter(status=Stock.IN_STOCK)


class OutOfStockStockListView(generics.ListAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        return Stock.objects.filter(status=Stock.OUT_OF_STOCK)
