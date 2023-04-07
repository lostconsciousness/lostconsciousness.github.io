import os
import django

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
os.environ.setdefault("DJANGO_SETTINGS_MODULE","pods.settings")
django.setup()

from aiogram import executor, Bot, Dispatcher, types
from newpost import areas_centers_names, find_warehouse
import requests
import json
import string
import random
from main.models import Offers

token = "6075679825:AAGrgD6b9hybk9EoNue44k1ZPW8paFJCs5M"






bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_fun(message: types.Message):
    print(message.from_user.username+": "+ message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kbbutton1 = types.KeyboardButton(text = "Так, мені є 18 років.")
    kbbutton2 = types.KeyboardButton(text = "Ні, мені ще немає 18 років.")
    keyboard.add(kbbutton1, kbbutton2)
    await message.answer('Вас вітає бот з продажу електронних сигарет! Чи є вам 18 років? ', reply_markup=keyboard) 

@dp.message_handler(lambda message: message.text == "Повернутися на минулий крок.")
async def startagain(message:types.Message):
    print(message.from_user.username+": "+ message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kbbutton1 = types.KeyboardButton(text = "Так, мені є 18 років.")
    kbbutton2 = types.KeyboardButton(text = "Ні, мені ще немає 18 років.")
    keyboard.add(kbbutton1, kbbutton2)
    await message.answer('Вас вітає бот з продажу електронних сигарет! Чи є вам 18 років? ', reply_markup=keyboard) 

@dp.message_handler(lambda message: message.text == "Ні, мені ще немає 18 років.")
async def no18(message:types.Message):
    print(message.from_user.username+": "+ message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kbbutton1 = types.KeyboardButton(text = "Повернутися на минулий крок.")
    keyboard.add(kbbutton1)
    await message.answer('Продаж нашої продукції дозволений лише людям що досягли повноліття.', reply_markup=keyboard) 

@dp.message_handler(lambda message: message.text == 'Так, мені є 18 років.') 
async def start_fun(message: types.Message):
    print(message.from_user.username+": "+ message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kbbutton1 = types.KeyboardButton(text = "Поділитися номером телефону.", request_contact=True)
    keyboard.add(kbbutton1)
    await message.answer('Надішліть, будь ласка, свій номер телефону: ', reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def qq(message:types.Message):
    print(message.from_user.username+": "+ message.contact.phone_number)
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text = "Site", web_app = types.WebAppInfo(url = "https://general2286.pythonanywhere.com/"))]
        ],
        resize_keyboard=True
    )
    reply_markup = types.InlineKeyboardMarkup()
    reply_markup.row(
        types.InlineKeyboardButton(
            text="Перейти до магазину",
            web_app=types.WebAppInfo(url="https://general2286.pythonanywhere.com/"),
        )
    )
    await bot.send_message(
        message.from_user.id,
        "Натисніть кнопку 'Перейти до магазину' та відкриється наш інтернет-магазин.",
        reply_markup=keyboard,
    )

@dp.message_handler(commands=['cities'])
async def spec(message:types.Message):
    print(message.from_user.username+": "+ message.text)
    s = "Усі обласні центри України:"
    for city in areas_centers_names:
        s = s+f"\n{city}"
    await message.answer(text=s)

@dp.message_handler(lambda message: message.text in areas_centers_names)
async def newpost(message:types.Message):
    print(message.from_user.username+": "+ message.contact.phone_number)
    s = "Усі відділення у місті "+message.text
    j = 0
    for i in find_warehouse(message.text):
        if j == 10:
            break
        j=j+1
        s = s + "\n"+i
    await message.answer(text=s)


@dp.message_handler(commands = ['pay'])
async def payment(message:types.Message):
    #print(message.from_user.username+": "+ message.contact.phone_number)
    print(int(message.text.split(" ")[1]))
    w4purl = "https://api.wayforpay.com/api"
    allObjects = ['Одноразовая электронная сигарета Airis Lux P5000 Pina Colada', 'Одноразовая электронная сигарета R&M Legend 10000 затяжек Big Bang Fruit', 'Одноразовая сигарета Joyetech VAAL MAX Lush Ice', 'Одноразовая сигарета Joyetech VAAL GLAZ6500 Passion Fruit Orange Guava', 'Одноразовая сигарета Joyetech VAAL EP4500 Cotton Candy', 'Одноразовая сигарета Joyetech VAAL EP4500 Peach Mango Watermelon', 'Одноразовая электронная сигарета Elf Bar BC3500 3500 затяжек Cranberry Grape', 'Chaser Salt for Pods 15 мл 50 мг (5.0%) Bali Triple Shot', 'Chaser Salt - Blackcurrant Menthol (Черная смородина с ментолом) 10мл 30 мг (3.0%)', '3Ger Salt 15 мл 35 мг (3,5%) Apple Caramel']
    random_elements = random.sample(allObjects, 5)
    new=[]
    for i in random_elements:
        i = i.replace("%", "")
        new.append(i)
    print(new)
    j = ""
    with open('txt.txt', 'r', encoding ='utf-8') as f:
        j = f.readline()
    data = {
    "transactionType":"CREATE_INVOICE",
    "merchantAccount":"test_merch_n1",
    "merchantAuthType":"SimpleSignature",
    "merchantDomainName":"www.market.ua",
    # "merchantSignature":"60c5d743b71f79abe48c7183ada4b451",
    "apiVersion":1,
    "language":"ru",
    "serviceUrl":"https://eovbu9r2zfhhsp8.m.pipedream.net",
    "orderReference":"DH167995721" + str(j),
    "orderDate":1415379863,
    "amount":int(message.text.split(" ")[1]),
    "currency":"UAH",
    "orderTimeout": 60,
    "productName": new,
    "productPrice":[1000,547, 432, 234, 324],
    "productCount":[1,1, 1,1,1],
    "paymentSystems": "card;privat24",
    "clientFirstName":"Bulba",
    "clientLastName":"Taras",
    "clientEmail":"rob@mail.com",
    "clientPhone":"380556667788"
    }
    print(type(j))
    print(j)
    j= int(j)+1
    with open('txt.txt', 'w') as f:
        f.write(str(j))
    # response=requests.get(f'https://wiki.wayforpay.com/wiki/default/generate-hmac?string=test_merch_n1%3Bwww.market.ua%3BDH1679956997%3B1415379863%3B158%3BUAH%3B%D0%9F%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81%D0%BE%D1%80%20Intel%20Core%20i5-4670%203.4GHz%3B%D0%9F%D0%B0%D0%BC%D1%8F%D1%82%D1%8C%20Kingston%20DDR3-1600%204096MB%  productPrice   20PC3-12800%3B1%3B1%3B1000%3B547&key=flk3409refn54t54t*FNJRET')
    def create_signature(data:dict):
        print(f'https://wiki.wayforpay.com/wiki/default/generate-hmac?string={data["merchantAccount"]}%3B{data["merchantDomainName"]}%3B{data["orderReference"]}%3B{data["orderDate"]}%3B{data["amount"]}%3B{data["currency"]}%3B{"%3B".join(data["productName"])}%3B{"%3B".join(str(i) for i in data["productCount"])}%3B{"%3B".join(str(i) for i in data["productPrice"])}&key=flk3409refn54t54t*FNJRET')
        response=requests.get(f'https://wiki.wayforpay.com/wiki/default/generate-hmac?string={data["merchantAccount"]}%3B{data["merchantDomainName"]}%3B{data["orderReference"]}%3B{data["orderDate"]}%3B{data["amount"]}%3B{data["currency"]}%3B{"%3B".join(data["productName"])}%3B{"%3B".join(str(i) for i in data["productCount"])}%3B{"%3B".join(str(i) for i in data["productPrice"])}&key=flk3409refn54t54t*FNJRET')
        return response.text
    signature=create_signature(data)
    data["merchantSignature"]=signature
    print(w4purl)

    response = requests.post(w4purl, json.dumps(data))
    json_obj = json.loads(response.text)
    w4purl = json_obj["invoiceUrl"].replace("\\","")
    reply_markup = types.InlineKeyboardMarkup()
    reply_markup.row(
        types.InlineKeyboardButton(
            text="Сплатити",
            url=w4purl,
        )
    )
    await message.answer(text = "натисніть кнопку сплати", reply_markup=reply_markup)



@dp.message_handler(content_types=types.ContentType.ANY)
async def spec(message:types.Message):
    
    try:
        Offers.objects.all()
        user_info = json.loads(message.web_app_data.data)
        offer = Offers(
            username = message.from_user.username,
            offer = user_info['offer'],
            amount = user_info['amount'],
            name = user_info['name'],
            phone_number = user_info['phone_number'],
            area = user_info['area'],
            city = user_info['city'],
            warehouse = user_info['warehouse']
                     )
        offer.save()
        print(offer.name)
        await message.answer(text =json.loads(message.web_app_data.data)['message'])
    except:
        print("sosunok")
        #print(message.from_user.username+": "+ message.text)








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)