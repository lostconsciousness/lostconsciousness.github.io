from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import path
from django.shortcuts import render, redirect
from django import forms
from .models import *
from bs4 import BeautifulSoup
from utils import DBManager
from django.http import HttpResponseRedirect
from django.contrib import messages
from decimal import Decimal, InvalidOperation
from django.template.response import TemplateResponse


# class XmlImportForm(forms.Form):
#     xml_upload = forms.FileField()

#start
class PodikForm(forms.Form):

    new_price = forms.CharField(max_length=255)
class PodikAdmin(admin.ModelAdmin):
    actions = ['update_price']

    def update_price(self, request, queryset):
        if request.method == 'POST':
            new_price = request.POST.get('new_price')  # Получаем значение новой цены из POST-запроса

            if not new_price:
                self.message_user(request, "Вы не ввели новую цену")  # Выводим сообщение, если значение не было введено
            else:
                queryset.update(price=new_price)
                self.message_user(request, f"Цена успешно обновлена на {new_price}")  # Выводим сообщение об успешном обновлении
                return redirect(request.get_full_path())  # Перенаправляем обратно на страницу со списком объектов

        context = {
            'opts': self.model._meta,
            'app_label': self.model._meta.app_label,
        }

        return TemplateResponse(request, 'admin/change_list.html', context)
    update_price.short_description = "Обновить цену на указанное значение"
    #end


    list_display = ('id','name','price', 'currencyId', 'available', 'param', 'get_html_photo')
    list_display_links = ('id','name','price', 'available', 'currencyId')
    search_fields = ('id','name', 'price', 'param')
    list_filter = ('available',)
    fields = ('name', 'id', 'available', 'price', 'currencyId', 'categoryId', 'vendorCode', 'quantity_in_stock', 'url', 'picture', 'get_html_photo', 'flavour' , 'nicotine_strength', 'fluid_volume', 'battery_capacity', 'cartridge_capacity', 'resistance', 'power', 'atomizer_volume', 'max_power', 'puffs_number', 'rechargeable', 'compatibility_selection')
    readonly_fields = ('get_html_photo', )
    def get_html_photo(self, object):
        return mark_safe(f"<img src = {object.picture} width = 50>")
    
    get_html_photo.short_description = 'Фото'
 
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-xml/', self.upload_xml),]
        return new_urls + urls
    
    def upload_xml(self, request):
        if request.method == "POST":
            xml_file = request.FILES["xml_upload"]
            # with open(xml_file,'r') as f:
            #     data = f.read()
            # tree = ET.parse(xml_file)
            # root = tree.getroot()
            file_data = xml_file.read().decode()
            with open('offer.xml', 'w', encoding='utf-8') as f:
                f.write(file_data)


            dbm = DBManager()
            dbm.addXmlToDB()


            # with open('offer.xml', 'r', encoding='utf-8') as f:
            #     data = f.read()
            # bs_data = BeautifulSoup(data, "xml")
            # print(type(bs_data.find('offer').find('vendorCode').text))
            # print(type(bs_data.find('offer')['available']))
            # offers = file.getElementsByTagName('name')
        form = XmlImportForm()
        data = {"form": form}
        return render(request, "admin/xml_upload.html", data)
# 




admin.site.register(Podik, PodikAdmin)
admin.site.site_title = 'сторінка адміністрації'
admin.site.site_header = 'Cторінка адміністрації'