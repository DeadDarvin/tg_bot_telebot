import telebot
from telebot.types import CallbackQuery
from telebot.types import Message
from telebot.util import quick_markup

import constans
from texts.user_texts import APPLICATION_TEXT
from texts.user_texts import START_TEXT
from texts.user_texts import TEXT_FOR_INSTRUCTION

bot = telebot.TeleBot(token=constans.BOT_TOKEN)  # Fix me

markup = quick_markup(
    {
        "Как отправить обращение?": {"callback_data": "query_get_instruction"},
        "Подробнее про Евгению": {"url": "https://facebook.com"},
    }
)


@bot.message_handler(commands=["start", "help"])
def start(message: Message):
    photo = open(f"{constans.BASE_DIR}/img/Asterizm-Bolshoj-Kovsh.jpg", "rb")
    bot.send_photo(
        chat_id=message.chat.id, photo=photo, caption=START_TEXT, reply_markup=markup
    )


def reply_after_application(chat_id):
    bot.reply_to(chat_id, text="Спасибо за обращение!")


@bot.message_handler(commands=["application"])
def get_application_from_chat(message: Message):
    bot.send_message(chat_id=message.chat.id, text=APPLICATION_TEXT)
    bot.register_next_step_handler_by_chat_id(
        message.chat.id, callback=reply_after_application
    )


@bot.callback_query_handler(func=lambda call: call.data == "query_get_instruction")
def send_application_instruction_in_chat(call: CallbackQuery):
    photo = open(f"{constans.BASE_DIR}/img/Python_mem.jpeg", "rb")
    bot.send_photo(call.message.chat.id, photo=photo, caption=TEXT_FOR_INSTRUCTION)
