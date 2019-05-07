from django.db import models
from django.db.models import CASCADE

from manufacturer.models import Manufacturer

# Create your models here.

class CandyCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Candy(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(CandyCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=CASCADE)
    def __str__(self):
        return self.name

class CandyImage(models.Model):
    image = models.CharField(max_length=999)
    candy = models.ForeignKey(Candy, on_delete=models.CASCADE)