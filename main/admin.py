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
from django.http import JsonResponse
from localStoragePy import localStoragePy
from .forms import UpdatePriceForm
from django.db.models import QuerySet
#localStorage = localStoragePy('general2286.pythonanywhere.com', 'db.sqlite3')


class XmlImportForm(forms.Form):
    xml_upload = forms.FileField()

#start
class PriceForm(forms.Form):
    price = forms.CharField(max_length=255)

class OffersAdmin(admin.ModelAdmin):
    list_display = ('offer_id','username','phone_number', 'name','offer', 'amount', 'area', 'city', 'warehouse','payment_method', 'delivery_method', 'comment')
    list_display_links = ('offer_id','username','phone_number', 'name','offer', 'amount', 'area', 'city', 'warehouse','payment_method', 'delivery_method', 'comment')
    readonly_fields = ('offer_id','username','phone_number', 'name','offer', 'amount', 'area', 'city', 'warehouse', 'products', 'comment', 'payment_method', 'delivery_method')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username','phone_number', 'name')
    list_display_links = ('username','phone_number', 'name')
    readonly_fields = ('username','phone_number', 'name')


class PodikAdmin(admin.ModelAdmin):
    actions = ['update_price']
    # def update_price(self, request, queryset):
    #     # Перенаправляет на страницу обновления цены.
    #     return HttpResponseRedirect(reverse('admin:update_price', args=[queryset.values_list('id', flat=True)]))
    # update_price.short_description = 'Обновить цену'
    def update_price(self, request, queryset: QuerySet):
        # Перенаправляет на страницу обновления цены.
        # return HttpResponseRedirect(reverse('update_price', args=[queryset.values_list('id', flat=True)])) 
        form = UpdatePriceForm()
        # print(list(queryset))
        j=0
        data_dict={}
        for i in queryset:
            data_dict[f"id{j}"]=i.id
            j+=1
        # print(data_dict)
        return render(request, 'admin/update_price.html', {"my_data":data_dict, 'form': form})
    update_price.short_description = "Оновити параметри"
    #end


    list_display = ('id','name','price', 'currencyId', 'available', 'quantity_in_stock','param',  'get_html_photo')
    list_display_links = ('id','name','price', 'available', 'quantity_in_stock','currencyId')
    search_fields = ('id','name', 'price', 'param', 'picture')
    list_filter = ('available',)
    fields = ('name', 'id', 'available', 'price', 'currencyId', 'categoryId', 'vendorCode', 'quantity_in_stock', 'url', 'picture', 'get_html_photo', 'flavour' , 'nicotine_strength', 'fluid_volume', 'battery_capacity', 'cartridge_capacity', 'resistance', 'power', 'atomizer_volume', 'max_power', 'puffs_number', 'rechargeable', 'compatibility_selection')
    readonly_fields = ('get_html_photo', )
    def get_html_photo(self, object):
        return mark_safe(f"<img src = {object.picture} width = 50>")
    
    get_html_photo.short_description = 'Фото'
 
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-xml/', self.upload_xml), path('update-price/', self.update_price)]
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
admin.site.register(Offers, OffersAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.site_title = 'сторінка адміністрації'
admin.site.site_header = 'Cторінка адміністрації'