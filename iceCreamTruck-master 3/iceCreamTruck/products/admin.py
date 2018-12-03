from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('flavor_name', 'flavor_id', '_price', 'quantity_stocked', 'date_created', 'date_updated',)
    list_filter = ('date_created','date_updated', 'price',)
    
admin.site.register(Product, ProductAdmin)
