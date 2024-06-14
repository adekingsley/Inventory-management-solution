from django.contrib import admin

from items.models import Item


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Item, ItemAdmin)
