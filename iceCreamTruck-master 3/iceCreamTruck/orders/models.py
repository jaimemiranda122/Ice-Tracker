import datetime

from django.db import models
from django.utils import timezone
from customers.models import Customer
from products.models import Product
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete 
from django.dispatch import receiver

class OrderForm(models.Model):
    order_i_d = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,) 
    flavor = models.ForeignKey(Product, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    
    def clean(self):
        if self.quantity > self.flavor.quantity_stocked:
            raise ValidationError('Not enough product stocked.')
            
    def save(self, *args, **kwargs):
        sold = self.flavor.quantity_stocked - self.quantity
        self.flavor.quantity_stocked = sold
        self.flavor.save()
        super(OrderForm, self).save(*args, **kwargs)
    
    @receiver(pre_delete)
    def delete_repo(sender, instance, **kwargs):
        unsold = instance.flavor.quantity_stocked + instance.quantity
        instance.flavor.quantity_stocked = unsold
        instance.flavor.save()
           
    def __str__(self):
        return '%s' % (str(self.order_i_d).zfill(6),)
    
    @property
    def _product_id(self):
        return '%s' % (str(self.flavor.flavor_i_d).zfill(6),)
        
    @property
    def total_cost(self):
        return '$%s' % (self.quantity * self.flavor.price)
    
    @property
    def name(self):
        return '%s %s' % (self.customer.first_Name, self.customer.last_Name)
        
    @property
    def _customer_id(self):
        return '%s' % (str(self.customer.customer_i_d).zfill(6),)

    @property
    def _order_id(self):
        return '%s' % (str(self.order_i_d).zfill(6),)
