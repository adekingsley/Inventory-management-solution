from django.contrib import admin

from stock.models import Stock


# Register your models here.
class StockAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'created_at', 'updated_at')
    search_fields = ('item__name',)
    list_filter = ('item',)


admin.site.register(Stock, StockAdmin)
