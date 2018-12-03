import datetime

from django.db import models
from django.utils import timezone

class Product(models.Model):
    flavor_i_d = models.AutoField(primary_key=True)
    flavor_name = models.CharField(max_length = 20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_stocked = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    
    @property
    def _price(self):
        return "$%s" % self.price
    
    @property
    def flavor_id(self):
        return '%s' % (str(self.flavor_i_d).zfill(6),)

    def __str__(self):
        return '%s' % (self.flavor_name)
