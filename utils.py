import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE","pods.settings")
django.setup()

from main.models import Podik
import json


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
                description=pod["description"][0],
                quantity_in_stock=int(pod["quantity_in_stock"][0]),
                url=pod["url"][0],
                picture=pod["picture"][0],
                # param=pod["param"][0]["_"],
            )
            podik.save()

dbm = DBManager()
dbm.addToDB()