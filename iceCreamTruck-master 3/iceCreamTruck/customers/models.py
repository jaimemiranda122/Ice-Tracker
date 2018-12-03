import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class Customer(models.Model):   
    state_list =(('AL','AL'), ('AK','AK'), ('AZ','AZ'), ('AR','AR'), ('CA','CA'), ('CO','CO'), ('CT','CT'), ('DC','DC'), ('DE','DE'), ('FL','FL'), ('GA','GA'), ('HI','HI'), ('ID','ID'), ('IL','IL'), ('IN','IN'), ('IA','IA'), ('KS','KS'), ('KY','KY'), ('LA','LA'), ('ME','ME'), ('MD','MD'), ('MD','MD'), ('MI','MI'), ('MN','MN'), ('MS','MS'), ('MO','MO'), ('MT','MT'), ('NE','NE'), ('NV','NV'), ('NH','NH'), ('NJ','NJ'), ('NM','NM'), ('NY','NY'), ('NC','NC'), ('ND','ND'), ('OH','OH'), ('OK','OK'), ('OR','OR'), ('PA','PA'), ('RI','RI'), ('SC','SC'), ('SD','SD'), ('TN','TN'), ('TX','TX'), ('UT','UT'), ('VT','VT'), ('VA','VA'), ('WA','WA'), ('WV','WV'), ('WI','WI'), ('WY','WY'))
    customer_i_d = models.AutoField(primary_key=True)
    first_Name = models.CharField(max_length = 25)
    last_Name = models.CharField(max_length = 25)
    street_Address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length=2,choices=state_list,)
    zip_Code = models.CharField(max_length = 5, validators=[RegexValidator('^\d{5}$')])
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    
    @property
    def customer_id(self):
        return '%s' % (str(self.customer_i_d).zfill(6),)
        
    def __str__(self):
        return '%s %s %s' % (str(self.customer_id).zfill(6), self.first_Name, self.last_Name)
