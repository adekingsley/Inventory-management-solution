from django.contrib import admin

from suppliers.models import Supplier


# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'contact_email', 'contact_phone')
    search_fields = ('name', 'contact_name', 'contact_email')
    list_filter = ('name',)


admin.site.register(Supplier, SupplierAdmin)
