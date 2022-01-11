import telebot
import db as pg
import kpadapter
import config
from telebot import types

import urlparse

TOKEN = "2110122103:AAERC4s9rn6sRUXFAhNv61Y7aCB5dazMlcQ"

bot = telebot.TeleBot(TOKEN)



def check_user(message):
    return message.from_user.id in config.users

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    if check_user(message):
        bot.send_message(message.chat.id, f"Отправьте ссылку на фильм на кинопоиске для добавления в список")
    else:
        bot.send_message(message.chat.id, f"private data")


@bot.message_handler(commands=['random'])
def get_film_list(message):
    if check_user(message):
        film = pg.get_film_data(pg.get_random_film())
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton(f"Смотреть {film['id']}")
        itembtn2 = types.KeyboardButton('Отложить')
        itembtn3 = types.KeyboardButton(f"Удалить {film['id']}")
        markup.add(itembtn1, itembtn2,itembtn3)

        msg = bot.send_photo(message.chat.id,film['image'],f"{film['name']}({film['year']}) {film['duration']} мин. \n{film['description']}",reply_markup=markup)


    else:
        bot.send_message(message.chat.id, f"private data")




@bot.message_handler(commands=['list'])
def get_film_list(message):
    if check_user(message):
        bot.send_message(message.chat.id, pg.get_film_list())
    else:
        bot.send_message(message.chat.id, f"private data")

@bot.message_handler(content_types=['text'])
def parse_message(message):
    if check_user(message):
        try:
            if str(message.text).startswith('www'):
                kpadapter.save_film_info_url(message.text)
                bot.send_message(message.chat.id, 'Фильм добавлен в список. Для просмотра списка выполните команду /list')
            elif str(message.text).startswith('Смотреть') or str(message.text).startswith('Удалить'):
                pg.delete_film(urlparse.get_film_id_from_message(message.text))
                bot.send_message(message.chat.id,'Фильм удален из списка')
        except Exception as e:
            print(e)
    else:
        bot.send_message(message.chat.id, f"private data")




bot.polling(none_stop=True)



