from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def contact_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Share contact', request_contact=True)
    kb.add(button)

    return kb

def start_chatGBT_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('START CHATGBT')
    kb.add(button)

    return kb

def save_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Save')
    kb.add(button)

    return kb