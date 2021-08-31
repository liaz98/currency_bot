import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import json
from telegram import Update



soup : BeautifulSoup
req = requests.get('https://nbu.uz/uz/exchange-rates/json/')
soup: BeautifulSoup = BeautifulSoup(req.text, features="lxml")
json_format = json.loads(req.text)
bot = telebot.TeleBot("1970240486:AAFmM-2WzJWR0Ii973XG2Np5I0V6etV8h2w")

@bot.message_handler(commands=['start'])
def currencies(message):
    markup = types.ReplyKeyboardMarkup(row_width=4)
    for data in json_format:
        item=types.KeyboardButton(data['title'])
        markup.add(item)
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def sections(message):
    for data in json_format:
        if message.text in data['title']:
            if data['nbu_cell_price'] is "":
                bot.send_message(message.chat.id, "MB: "+data['cb_price'])
            else:
                bot.send_message(message.chat.id, "Sotib olish:  " + data['nbu_buy_price']+"\n"+"Sotish:  "+data['nbu_cell_price']+"\n"+"MB:  "+data['cb_price'])

bot.polling()
