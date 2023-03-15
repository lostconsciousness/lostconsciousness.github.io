from django.db import models


class Podik(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    available = models.BooleanField()
    price = models.IntegerField()
    currencyId = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    categoryId = models.IntegerField()
    vendorCode = models.IntegerField()
    quantity_in_stock = models.IntegerField()
    description = models.TextField()
    url = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    # param = models.CharField(max_length=255)

# Create your models here.
