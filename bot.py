import telebot
import database
import buttons
import random
import openai
from buttons import contact_button, start_chatGBT_button
from database import check_user, register_user

openai.api_key = 'KEY'

TOKEN = '6303884335:AAGdJYFhOLfJhWUAuC7o4CLcfSKEMSWTAtY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    
    chek = database.check_user(message.from_user.id)

    if chek:
        bot.send_message(message.from_user.id, 'CHATGBT ishlatish', reply_markup=buttons.start_chatGBT_button())

    else:
        bot.send_message(message.from_user.id, 'Kantakt yuboring', reply_markup=buttons.contact_button())
        bot.register_next_step_handler(message, get_contact)

def get_contact(message):
    if message.contact:
        phone_number = message.contact.phone_number
        first_name = message.contact.first_name

        database.register_user(first_name, message.from_user.id, phone_number)

        bot.send_message(message.from_user.id, 'Registratsiyadan otdingiz', reply_markup=buttons.start_chatGBT_button())

    else:
        bot.send_message(message.from_user.id, 'Kantakt yuboring', reply_markup=buttons.contact_button())
        bot.register_next_step_handler(message, get_contact)


@bot.message_handler(content_types=['text'])
def text(message):

    Users = database.check_user(message.from_user.id)
    if message.text == 'start cahtgpt' and Users:
        reply = ''
        response = openai.ChatCompletion.create(
            model='gbt-3,5-turbo',
            messages=[{'role': 'Users', 'content': message.text}],
            timeout=15,
        )

        if response and response.choices:
            reply = response.choices[0]['message']['contect']

        else:
            reply = 'Nmagadur ChatGbt job bergisi kemayapti :('

        bot.send_message(message.from_user.id, reply)

    else:
        bot.send_message(message.from_user.id, "ChatGbt ni ishlatish uchun siz registratsiyadan otishingiz kerak")
        bot.register_next_step_handler(message, get_contact)


bot.polling()



# salom bu test