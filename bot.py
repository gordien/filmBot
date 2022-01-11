import telebot
import db as pg
import kpadapter

TOKEN = "2110122103:AAERC4s9rn6sRUXFAhNv61Y7aCB5dazMlcQ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, f"Отправьте ссылку на фильм на кинопоиске для добавления в список")
    pg.save_user_info(message.from_user.id, message.from_user.username)



@bot.message_handler(commands=['list'])
def get_film_list(message):
    bot.send_message(message.chat.id, *pg.get_film_list(message.from_user.id))

@bot.message_handler(content_types=['text'])
def parse_message(message):
    try:
        pg.add_film_to_list_db(kpadapter.save_film_info_url(message.text),message.from_user.id)
        bot.send_message(message.chat.id, 'Фильм добавлен в список. Для просомтра списка выполните команду /list')
    except Exception as e:
        print(e)




bot.polling(none_stop=True)

print(pg.user_exists(213213))

