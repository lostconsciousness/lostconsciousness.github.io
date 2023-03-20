from django.db import models
from django.urls import reverse


class Podik(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва продукту")
    id = models.CharField(max_length=255, primary_key=True)
    available = models.BooleanField(verbose_name="Доступність")
    price = models.IntegerField(verbose_name="Ціна")
    currencyId = models.CharField(max_length=255, verbose_name="Валюта")
    categoryId = models.IntegerField(verbose_name="Id категорії")
    vendorCode = models.IntegerField()
    quantity_in_stock = models.IntegerField(verbose_name="Кількість товару склад")
    #description = models.TextField(verbose_name="Опис")
    url = models.CharField(max_length=255)
    picture = models.CharField(max_length=255, verbose_name="URL картинки")
    # param = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Електронна цигарка"
        verbose_name_plural = "Електронні цигарки"
        ordering = ['categoryId', 'name']
    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

# Create your models here.
