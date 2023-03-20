from aiogram import executor, Bot, Dispatcher, types
from newpost import areas_centers_names, find_warehouse

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
        reply_markup=reply_markup,
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
    s = "Усі відділення у місті "+message.text
    j = 0
    for i in find_warehouse(message.text):
        if j == 10:
            break
        j=j+1
        s = s + "\n"+i
    await message.answer(text=s)

@dp.message_handler(content_types=types.ContentType.ANY)
async def spec(message:types.Message):
    print(message.from_user.username+": "+ message.text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)