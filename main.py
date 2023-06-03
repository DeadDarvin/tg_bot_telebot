import telebot
from telebot.types import Message

import constans

bot = telebot.TeleBot(token=constans.BOT_TOKEN)  # Fix me


@bot.message_handler(commands=['start', ])
def say_hello(message: Message):
    bot.reply_to(message=message, text='Hello World!')


bot.polling()