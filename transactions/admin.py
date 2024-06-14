from django.contrib import admin

from transactions.models import Purchase, Sale

# Register your models here.


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('item', 'supplier', 'quantity',
                    'price', 'total_amount', 'created_at')
    search_fields = ('item__name', 'supplier__name')
    list_filter = ('created_at',)


class SaleAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'total_amount', 'created_at')
    search_fields = ('item__name',)
    list_filter = ('created_at',)


admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Sale, SaleAdmin)
