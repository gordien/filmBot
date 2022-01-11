import telebot
import db as pg
import kpadapter
import config


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
        bot.send_photo(message.chat.id,film['image'],f"{film['name']}({film['year']}) {film['duration']} мин. \n  {film['description']}")

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
            kpadapter.save_film_info_url(message.text)
            bot.send_message(message.chat.id, 'Фильм добавлен в список. Для просомтра списка выполните команду /list')
        except Exception as e:
            print(e)
    else:
        bot.send_message(message.chat.id, f"private data")




bot.polling(none_stop=True)



