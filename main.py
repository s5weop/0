from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot('6350331021:AAFW9Zgm69WGYg9uIWpljeA1_n-h_wY_ARs')
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, 'HI')

@bot.message_handler(commands=['finish'])
async def afgshdjfs(message):
    await bot.reply_to(message, 'BYE')

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