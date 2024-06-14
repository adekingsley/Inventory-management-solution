from django.http import JsonResponse
from rest_framework import generics
from .models import Purchase, Sale
from .serializers import PurchaseSerializer, SalesSerializer
from django.views.decorators.csrf import csrf_exempt
# Purchase Views


class PurchaseCreateView(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseUpdateView(generics.UpdateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseDeleteView(generics.DestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseListView(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseDetailView(generics.RetrieveAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class ReadPurchaseByID(generics.RetrieveAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    lookup_field = "pk"


# Sales Views
class SalesCreateView(generics.CreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SalesSerializer


class SalesUpdateView(generics.UpdateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SalesSerializer


class SalesDeleteView(generics.DestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SalesSerializer


class SalesListView(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SalesSerializer


class SalesDetailView(generics.RetrieveAPIView):
    queryset = Sale.objects.all()
    serializer_class = SalesSerializer


class ReadSalesByID(generics.RetrieveAPIView):
    queryset = Sale.objects.all()
    serializer_class = SalesSerializer
    lookup_field = "pk"


@csrf_exempt
def delete_all_sales(request):
    try:
        # Get all sales and delete them
        sales = Sale.objects.all()
        for sale in sales:
            sale.delete()
        return JsonResponse({"message": "All sales deleted successfully."})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
