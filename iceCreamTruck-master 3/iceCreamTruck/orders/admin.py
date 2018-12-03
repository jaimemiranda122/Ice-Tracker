from django.contrib import admin

from .models import OrderForm

class OrderFormAdmin(admin.ModelAdmin):
    readonly_fields = ['total_cost',]
    list_display = ('_order_id', 'name', '_customer_id', 'flavor', 'quantity', 'total_cost', 'date_created', 'date_updated',)
    list_filter = ('date_created','date_updated', 'flavor', 'customer')

admin.site.register(OrderForm, OrderFormAdmin)
