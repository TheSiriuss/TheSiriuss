import telebot
from telebot import types
import random

bot = telebot.TeleBot('Супер секретный токен')


@bot.message_handler(commands=['get_start', 'start'])
def first_message(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Согласен', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='Не согласен', callback_data='no')
    item_secret = types.InlineKeyboardButton(text='Дальше', callback_data='secret')

    markup_inline.add(item_no, item_yes, item_secret)
    bot.send_message(message.chat.id, 'Привет, я TheSiriuss, а это мой личный чат-бот. ''\n'
                                      'Мой уровень создания ботов чуть выше нуля,''\n'
                                      'Поэтому чтобы вернуться в главное меню напиши: /start', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):

    markup_reply = types.ReplyKeyboardMarkup()
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Что да то? С чем ты соглашаешься шизик?', reply_markup=markup_reply)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Что нет то? С чем ты не согласен шизик? ', reply_markup=markup_reply)
    elif call.data == 'secret':
        pass


@bot.message_handler(content_types=['text'])
def back_track(message):
    x = random.randint(0, 1)
    if x == 0 and message.text == 'Скинь чё нить':
        bot.send_message(message.chat.id, 'Кого ты выберешь, нас или их, их или нас?')
    elif x == 1 and message.text == 'Скинь чё нить':
        bot.send_message(message.chat.id, 'Опа скереточка')
    else:
        bot.send_message(message.chat.id, 'Ты написал что то не то, поэтому я вывожу это сообщение')

bot.polling(none_stop=True, interval=0)
