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
    param = models.TextField(null=True)
    flavour = models.CharField(null = True,max_length=255, verbose_name="Выбор вкуса")
    nicotine_strength = models.CharField(null = True,max_length=255, verbose_name="Крепость никотина")
    fluid_volume = models.CharField(null = True,max_length=255, verbose_name="Объем жидкости")
    battery_capacity = models.CharField(null = True,max_length=255, verbose_name="Ёмкость аккумулятора")
    cartridge_capacity = models.CharField(null = True,max_length=255, verbose_name="Объём картриджа")
    resistance = models.CharField(null = True,max_length=255, verbose_name="Выбор сопротивления")
    power = models.CharField(null = True,max_length = 255, verbose_name="Мощность")
    atomizer_volume = models.CharField(null = True,max_length=255, verbose_name="Объем атомайзера")
    max_power = models.CharField(null = True,max_length=255, verbose_name="Максимальная мощность")
    puffs_number = models.CharField(null = True,max_length=255, verbose_name="Количество затяжек")
    rechargeable = models.BooleanField(null = True, verbose_name="Перезаряжаемые'")
    compatibility_selection = models.CharField(null = True,max_length=255, verbose_name="Выбор совместимости")


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Електронна цигарка"
        verbose_name_plural = "Електронні цигарки"
        ordering = ['categoryId', 'name']
    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})


# class Parameters(models.Model):
#     id = models.ForeignKey(Podik, on_delete = models.CASCADE, primary_key=True)
    



# Create your models here.
class NovaPost(models.Model):
    city = models.CharField(max_length=255)
    ref = models.CharField(max_length=37, primary_key=True)
    warehouses = models.TextField()
    mailboxes = models.TextField(null = True)
    area = models.CharField(max_length=255)
    isAreaCenter = models.BooleanField(default=False)


class Offers(models.Model):
    username = models.CharField(max_length=255, verbose_name="Ім'я користувача")
    offer = models.TextField(verbose_name="Замовлення")
    amount = models.CharField(max_length=255, verbose_name="Ціна")
    name = models.CharField(max_length=255, verbose_name="ПІБ")
    phone_number = models.CharField(max_length=255, verbose_name="Номер телефону")
    area = models.CharField(max_length=255, verbose_name="Область")
    city = models.CharField(max_length=255, verbose_name="Місто")
    warehouse = models.CharField(max_length=255, verbose_name="Пункт видачі")
    products = models.TextField(null = True)