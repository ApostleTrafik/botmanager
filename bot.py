import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = input('Token:\n')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    if message.chat['id'] != -487534964:
        keyboard = types.InlineKeyboardMarkup()
        btn1= types.InlineKeyboardButton(text="Связаться с менеджером", callback_data="manager")
        btn2 = types.InlineKeyboardButton(text="Прайс", callback_data="price")
        btn3 = types.InlineKeyboardButton(text="Канал",url='https://t.me/joinchat/CfWqqjtL9ldhNjYy')
        keyboard.add(btn1,btn2)
        keyboard.add(btn3)
        await bot.send_message(message.chat.id, "Здравствуйте, выберите что Вас интересует !",reply_markup=keyboard)
@dp.message_handler()
async def echo(message: types.Message):
    if message.chat['id'] != -487534964:
        print(message)
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Связаться с менеджером", callback_data="manager")
        btn2 = types.InlineKeyboardButton(text="Прайс", callback_data="price")
        btn3 = types.InlineKeyboardButton(text="Канал", url='https://t.me/joinchat/CfWqqjtL9ldhNjYy')
        keyboard.add(btn1, btn2)
        keyboard.add(btn3)
        await message.forward(-487534964)
        if message.from_user['username'] != None:
            await bot.send_message(-487534964,'@'+message.from_user['username'])
        await message.answer('''Менеджер скоро свяжется с Вами, ожидайте !
Так же обязательно подпишитесь на наш канал что бы не потерять нас !''',reply_markup=keyboard)
@dp.callback_query_handler()
async def btn_answer(call):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Связаться с менеджером", callback_data="manager")
    btn2 = types.InlineKeyboardButton(text="Прайс", callback_data="price")
    btn3 = types.InlineKeyboardButton(text="Канал",url='https://t.me/joinchat/CfWqqjtL9ldhNjYy')
    keyboard.add(btn1, btn2)
    keyboard.add(btn3)
    await call.answer(cache_time=60)
    callback_data = call.data
    if callback_data == 'price':
        await call.message.answer('''Рассылка/Инвайт/Акк/Софт/Блок

Поиск ЦА для Вашей услуги:
- Рассылка смс по ЦА в ЛС
- Инвайт ЦА к Вам в группу
- Парсинг групп/Баз номеров
- Свои поставщики баз номеров любой ЦА по ГЕО

Цены:
500 сообщений/инвайтов - 700р
1 000 сообщений/инвайтов - 1 300р
5 000 сообщений/инвайтов - 6 000р
10 000 сообщений/инвайтов - 10 500р


- Спамер + парсер аудиторий 8 000р навсегда
- Инвайтер + парсер 5 000р навсегда
- Авторегер акк тг 10 000р навсегда
- Спамер по чатам 1000смс в один чат за 3 минуты 7000р
- Спамер по базе номеров + парсер 10 000р
- Инвайтер по базе номеров + Парсер 7 000р
В подарок софт для проверки аккаунтов на бан.

Теги: #рассылка #спам #инвайт #софт #Блокировка''',reply_markup=keyboard)
    elif callback_data == 'manager':
        await call.message.answer('Напишите свой вопрос.')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)