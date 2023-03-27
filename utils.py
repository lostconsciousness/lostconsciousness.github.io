import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE","pods.settings")
django.setup()

from main.models import Podik
import json
from bs4 import BeautifulSoup
from django.db import transaction


class DBManager:
    def __str_to_bool(self,s):
        return s.lower() in ['true', '1', 't', 'y', 'yes']
    @transaction.atomic
    def addToDB(self):
        data = json.load(open("alldata.json", "r", encoding="UTF-8"))
        Podik.objects.all().delete()
        pods = data["yml_catalog"]["shop"][0]["offers"][0]["offer"]
        
        # print(pods[0]["$"])
        # print(self.__str_to_bool("false"))
        for pod in pods:
            picture = '-'
            try:
                picture=pod["picture"][0]
            except:
                picture="-"
            par = ""
            try:
                for parametr in pod['param']:
                    par =par + parametr["$"]["name"] + " = " + parametr["_"]+", "
            except:
                par = "-"
            flavour = '-'
            try:
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Выбор вкуса":
                        flavour=parametr["_"]
            except:
                flavour="-"
            nicotine_strength = '-'
            try:
                nicotine_strength = ''
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Крепость никотина" or parametr["$"]["name"] == "Выбор крепости":
                        for i in parametr["_"]:
                            if i.isdigit():
                                nicotine_strength = nicotine_strength+i
            except:
                nicotine_strength="-"
            nicotine_type = '-'
            try:
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Вид никотина":
                        nicotine_type = parametr["_"]
            except:
                nicotine_type="-"
            fluid_volume = '-'
            try:
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Объем жидкости":
                        fluid_volume = parametr["_"]
            except:
                fluid_volume="-"
            battery_capacity = '-'
            try:
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Ёмкость аккумулятора":
                        for i in parametr["_"].split(" "):
                            if i.isdigit():
                                battery_capacity = str(i) + " mAh"
            except:
                battery_capacity="-"
            cartridge_capacity = "-"
            try:
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Объём картриджа":
                        cartridge_capacity = parametr["_"]
            except:
                cartridge_capacity="-"

            resistance = '-'
            try:
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Выбор сопротивления":
                        resistance = parametr["_"]
            except:
                resistance="-"

            power = ""
            try:
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Мощность":
                        power = parametr["_"]
            except:
                power="-"
            atomizer_volume = "-"
            try:
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Объем атомайзера":
                        if parametr["_"][-1] != ".":
                            atomizer_volume = parametr["_"] + "."
                        else:
                            atomizer_volume = parametr["_"]
            except:
                atomizer_volume="-"

            max_power = "-"
            try:
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Максимальная мощность":
                        for i in parametr["_"].split(" "):
                            if i.isdigit():
                                max_power = str(i) + " Вт"
            except:
                max_power="-"

            puffs_number = "-"
            try:
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Количество затяжек" or parametr["$"]["name"] == "Выбор количества затяжек":
                        puffs_number = parametr["_"]
            except:
                puffs_number="-"

            rechargeable = None
            try:
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Перезаряжаемые":
                        if parametr["_"] == "Так":
                            rechargeable = True
                        else:
                            rechargeable = False
            except:
                rechargeable=None

            compatibility_selection = "-"
            try:
                for parametr in pod['param']:
                    if parametr["$"]["name"] == "Выбор совместимости":
                        compatibility_selection = parametr["_"]
            except:
                compatibility_selection="-"
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
                picture=picture,
                param=par,
                flavour = flavour,
                nicotine_strength = nicotine_strength[:2],
                fluid_volume = fluid_volume,
                battery_capacity = battery_capacity,
                cartridge_capacity = cartridge_capacity,
                resistance = resistance,
                power = power,
                atomizer_volume = atomizer_volume,
                max_power = max_power,
                puffs_number = puffs_number,
                rechargeable = rechargeable,
                compatibility_selection = compatibility_selection,
            )
            podik.save()
    def check(self):
        data = json.load(open("alldata.json", "r", encoding="UTF-8"))
        pods = data["yml_catalog"]["shop"][0]["offers"][0]["offer"]
        povtorenie = []
        id_povtorenia = []
        params = []
        # print(pods[0]["$"])
        for pod in pods:
            try:
                params = pod["param"]
                for param in params:
                    if pod["categoryId"][0]+": "+ param["$"]['name'] not in id_povtorenia:
                        povtorenie.append(param["$"]['name'])
                        id_povtorenia.append(pod["categoryId"][0]+": "+ param["$"]['name'])
            except:
                pass
                
        #print(povtorenie)
        print(id_povtorenia)
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
                #params=pod["param"][0]["_"],
            )
            podik.save()
        
dbm = DBManager()
#dbm.check()
#dbm.addToDB()
# dbm.addXmlToDB()