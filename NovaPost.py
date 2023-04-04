import requests
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","pods.settings")
django.setup()

from main.models import NovaPost



URL = 'https://api.novaposhta.ua/v2.0/json/'
API_KEY = '9fca35c6a673642fc96b4bbccc542ad3'

def get_areas():
   areas_centers=[]
   params = {
      "apiKey": API_KEY,
      "modelName": "Address",
      "calledMethod": "getAreas",
      "methodProperties": {   }
   }

   response = requests.post(URL, json=params)
   result = response.json()

   i = 0
   if 'data' in result:
      areas = result['data']
      for area in areas:
         areas_centers.append(area['AreasCenter'])
         i = i + 1
   else:
      print(result['errors'])
   
   return areas_centers

def get_areas_centers():
   areas_centers = get_areas()
   areas_centers_names = []

   params = {
      'apiKey': API_KEY,
      'modelName': 'Address',
      'calledMethod': 'getCities',
      "methodProperties": {
         "Page" : f"{0}"
      }
   }

   response = requests.post(URL, json=params)
   result = response.json()

   if 'data' in result:
      areas = result['data']
      for area in areas:
         if area['Ref'] in areas_centers:
               areas_centers_names.append(area['Description'])
               
   else:
      print(result['errors'])

   return areas_centers_names

def get_cities_and_add_to_db():
   NovaPost.objects.all().delete()
   cities = []
   area_centers = get_areas_centers()
   print(area_centers)

   i = 0
   while True:
      city = {}
      params = {
         "apiKey": API_KEY,
         "modelName": "Address",
         "calledMethod": "getSettlements",
         "methodProperties": {
         "Page":f"{i}"
         }
      }

      response = requests.post(URL, json=params)
      result = response.json()

      if 'data' in result:
         if len(result['data']) == 0:
            break
         cities_ = result['data']
         for city_ in cities_:
            if city_['SettlementTypeDescription'] != 'місто':
               continue
            warehouses = get_warehouses(city_['Ref'])
            if warehouses == '':
               continue
            novapost = NovaPost(city=city_['Description'], ref=city_['Ref'], area=city_['AreaDescription'], warehouses=warehouses, isAreaCenter=(True if city_['Description'] in area_centers else False))
            novapost.save()
            city['name'] = city_['Description'].replace('`', '').replace("'", "").replace('\'', '').replace('"', '')
            city['Ref'] = city_['Ref']
            city['Area'] = city_['AreaDescription'].replace('`', '').replace("'", '').replace('\'', '').replace('"', '')
            city['warehouses'] = warehouses.replace('`', '').replace("'", '').replace('\'', '').replace('"', '')
            cities.append(city)
            print(city)
      i+=1
   return cities
      

def get_warehouses(ref):
   i = 1
   warehouses = ''
   while True:
      params = {
      "apiKey": API_KEY,
      "modelName": "Address",
      "calledMethod": "getWarehouses",
      "methodProperties": {
         "SettlementRef": ref,
         "Page" : f"{i}",
         }
      }
      response = requests.post(URL, json=params)
      result = response.json()

      if 'data' in result:
         if len(result['data']) == 0:
            break
         warehouses_ = result['data']
         for house in warehouses_:
            if 'Поштомат' not in house['Description']:
               warehouses += house['Description'].replace('`', '').replace("'", '').replace('\'', '').replace('"', '') + ';'
      i+=1
   return warehouses

print(get_cities_and_add_to_db())
# print(get_areas_centers())