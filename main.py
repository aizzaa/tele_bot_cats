from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from decouple import config


token = config('TOKEN')

bot = TeleBot(token)


@bot.message_handler(['start', 'hi', 'hello'])
def start_message(message: Message):
    bot.send_message(message.chat.id, f'Привет, {message.chat.username}')

@bot.message_handler(func=lambda message: message.text == 'кнопки')
def get_buttons(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('кнопка 1')
    button2 = KeyboardButton('кнопка 2')
    keyboard.add(button1, button2)

    bot.send_message(message.chat.id, 'нажми на кнопку', reply_markup=keyboard)


@bot.message_handler(func=lambda m: m.text == 'кнопка 1')
def inline_buttons(message: Message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('hello', callback_data='call1')
    button2 = InlineKeyboardButton('goodbye', callback_data='call2')
    keyboard.add(button1, button2)


    bot.reply_to(message, 'Держи кнопки в сообщении', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda c: True)
def handle_callback_data(callback: CallbackQuery):
    if callback.data == 'call2':
        bot.send_sticker(callback.message.chat.id, sticker='CAACAgIAAxkBAAEJ91Bk05bJ2TEv7wABxMlg9VjV9gk9dsQAArYTAAI_N-lL3iz_E7FAtS8wBA')
    else:
        bot.send_sticker(callback.message.chat.id, sticker='CAACAgIAAxkBAAEJ925k05cpv2a2maUwkwV-o1ty20dTSwAChxoAAr1NOEq9sPjp-eU-CTAE')
bot.infinity_polling()