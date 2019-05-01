from django.db import models as model
from datetime import datetime
from realtors.models import Realtor

class Listing(model.Model):
    realtor=model.ForeignKey(Realtor, on_delete=model.DO_NOTHING)
    title=model.CharField(max_length=200)
    address=model.CharField(max_length=200)
    city=model.CharField(max_length=100)
    state=model.CharField(max_length=100)
    zipcode=model.CharField(max_length=20)
    description=model.TextField(blank=True)
    price=model.IntegerField()
    bedrooms=model.IntegerField()
    bathrooms=model.DecimalField(max_digits=2,decimal_places=1)
    garage=model.CharField(default=0,max_length=10)
    sqft=model.IntegerField()
    lot_size=model.DecimalField(max_digits=5,decimal_places=1)
    photo_main=model.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo1=model.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo2=model.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo3=model.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo4=model.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo5=model.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo6=model.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published=model.BooleanField(default=True)
    list_date=model.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
