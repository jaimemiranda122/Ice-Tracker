from django.contrib import admin

from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_Name', 'last_Name', 'city', 'state', 'date_created', 'date_updated',)
    list_filter = ('date_created', 'date_updated',)


admin.site.site_header = 'Cream Blue Incorporated'
admin.site.index_title = 'Welcome'
admin.site.site_title = 'Cream Blue'
admin.site.register(Customer, CustomerAdmin)
