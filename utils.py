import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE","pods.settings")
django.setup()

from main.models import Podik
import json
from bs4 import BeautifulSoup


class DBManager:
    def __str_to_bool(self,s):
        return s.lower() in ['true', '1', 't', 'y', 'yes']
    def addToDB(self):
        data = json.load(open("podiki.json", "r", encoding="UTF-8"))

        pods = data["yml_catalog"]["shop"][0]["offers"][0]["offer"]
        print(pods[0]["$"])
        print(self.__str_to_bool("false"))
        for pod in pods:
            podik = Podik(
                id = pod["$"]["id"],
                available = self.__str_to_bool(pod["$"]["available"]),
                price = int(pod["price"][0]),
                currencyId =pod["currencyId"][0],
                name=pod["name"][0],
                categoryId=int(pod["categoryId"][0]),
                vendorCode=int(pod["vendorCode"][0]),
                # description=pod["description"][0],
                quantity_in_stock=int(pod["quantity_in_stock"][0]),
                url=pod["url"][0],
                picture=pod["picture"][0],
                # param=pod["param"][0]["_"],
            )
            podik.save()
    def addXmlToDB(self):
        with open('offer.xml', 'r',encoding='utf-8') as f:
            data = f.read()
        bs_data = BeautifulSoup(data, "xml")
        pods = bs_data.find_all('offer')
        for pod in pods:
            podik = Podik(
                id = pod['id'],
                available = self.__str_to_bool(pod["available"]),
                price = int(pod.find('price').text),
                currencyId = pod.find('currencyId').text,
                name = pod.find('name').text,
                categoryId=int(pod.find('categoryId').text),
                vendorCode=int(pod.find('vendorCode').text),
                # description=pod.find('description').text,
                quantity_in_stock=int(pod.find('quantity_in_stock').text),
                url=pod.find('url').text,
                picture=pod.find('picture').text,
                # param=pod["param"][0]["_"],
            )
            podik.save()
        
dbm = DBManager()
dbm.addToDB()
# dbm.addXmlToDB()