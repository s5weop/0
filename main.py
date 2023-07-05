import os

from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')

bot = AsyncTeleBot(TOKEN, parse_mode='HTML')
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, 'HI')
    chat_id = message.from_user.id
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('1')
    markup.add('2')
    await bot.send_message(chat_id, 'Меню', reply_markup=markup)

# def generate_markup(buttons, row):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     markup.add(*buttons, row_width=row) #* рспаковка список
#     return markup
# создать такую же функцию только с ниже штукой
# def generate_markup(buttons):
#     markup= InlineKeyboardMarkup()
    # for #распаковка словаря
    # markup.add(#словарь)
    # return markup

# @bot.message_handler(commands=['start'])
# async def send_welcome(message):
#     chat_id = message.from_user.id
    # markup = InlineKeyboardMarkup()
    # b1 = InlineKeyboardButton('1', callback_data='first')
    # b2 = InlineKeyboardButton('2', callback_data='second')
    # b3 = InlineKeyboardButton('3', callback_data='third')
    # markup.add(b1)
    # markup.add(b2)
    # markup.add(b3)
    # buttons={'1':'first',
    #          '2':'second',
    #          '3':'third'} #?? не знаю как правильно сделать словарь
    # await bot.send_message(chat_id, '1 var', reply_markup=markup)

    # buttons = ['1', '2', '3']
    # await bot.send_message(chat_id, '2 var', reply_markup=generate_markup(buttons, 2))


@bot.message_handler(commands=['s'])
async def afgshdjfs(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_message(chat_id, 'таймер 5 сек')
    for i in range(1,6):
        await asyncio.sleep(1)
        await bot.edit_message_text(f'{5-i} секунд осталось', chat_id, bot_message.id)
    await bot.delete_message(chat_id, bot_message.id)

    #await bot.send_location(chat_id, 58.00257, 56.25083)

    #await bot.send_document(chat_id, open('text.txt', 'rb'))

    #await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAIiKGSkCzv5ENDVE8I17WUxkAABm7KPDAACUxUAAuZ0aEi8VpxgvWUv2S8E')

    #await bot.send_message(chat_id, 'sssssss', disable_notification=True, protect_content=True)

    #bot_message = await bot.send_dice(chat_id, '🎰')
    #print(bot_message.dice.value)

@bot.message_handler(commands=['t'])
async def font(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<i>курсив</i>')
    await bot.send_message(chat_id, '<b>жирный</b>')
    await bot.send_message(chat_id, '<u>подчеркивание</u>')
    await bot.send_message(chat_id, '<s>зачеркивание</s>')
    await bot.send_message(chat_id, '<code>моноширинный1</code>')
    await bot.send_message(chat_id, '<pre>моноширинный2</pre>')
    await bot.send_message(chat_id, '<tg-spoiler>спойлер</tg-spoiler>')
    await bot.send_message(chat_id, '<a href="https://github.com/">гиперссылка</a>')
    await bot.send_message(chat_id, '<a href="tg://user?id=777000">пользователь</a>')

@bot.message_handler(content_types=["text"])
async def draznilka(message):
    chat_id = message.from_user.id
    await bot.delete_message(chat_id, message.id)


@bot.message_handler(func=lambda message: True)
async def echo(message):
    text=message.text
    text = text.lower()
    if 'дел' in text or 'настроение' in text:
        await bot.reply_to(message, 'хорошо')
    elif 'шутк' in text:
        await bot.reply_to(message, 'колоок повесился')
    else:
        await bot.reply_to(message, 'не понял')



import asyncio
asyncio.run(bot.polling())