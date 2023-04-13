import os
import django

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
os.environ.setdefault("DJANGO_SETTINGS_MODULE","pods.settings")
django.setup()

import requests
from main.models import Podik, Offers
import json

def to_sales_drive():
    offers = Offers.objects.all()
    offer = offers[len(offers)-1]
    products = []
    for product in offer.products.split(';'):
        print(product)
        if product.split(":")[0] != "":
            products.append(
                {"id": product.split(":")[0], "name": product.split(":")[1], "costPerItem": product.split(":")[2], "amount" : product.split(":")[3]},
                )
    print(products)
    if len(offer.name.split(' '))>1:
        response = requests.post('https://general2286.salesdrive.me/handler/', json={
            "form":"SDmlHVjXAGrbtIArLI0j1fb115xbM9rF_krtzXsld5CG96A6FfqzJ9z",
            "getResultData": "",
            "products": products,
            "fName": offer.name.split(' ')[1],
            "lName": offer.name.split(' ')[0],
            "phone": offer.phone_number,
            })
    else:
        response = requests.post('https://general2286.salesdrive.me/handler/', json={
            "form":"SDmlHVjXAGrbtIArLI0j1fb115xbM9rF_krtzXsld5CG96A6FfqzJ9z",
            "getResultData": "",
            "products": products,
            "fName": offer.name,
            "phone": offer.phone_number,
            })
    print(response.text)

# to_sales_drive()