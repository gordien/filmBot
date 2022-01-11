import telebot
import db as pg

TOKEN = "2110122103:AAERC4s9rn6sRUXFAhNv61Y7aCB5dazMlcQ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, f"Отправьте ссылку на фильм на кинопоиске для добавления в список")
    pg.save_user_info(message.from_user.id,message.from_user.username)



@bot.message_handler(commands=['list'])
def get_film_list(message):
    bot.send_message(message.chat.id, "Люблю Печенку")

@bot.message_handler(content_types=['text'])
def parse_url(message):
    bot.send_message(message.chat.id, message)



bot.polling(none_stop=True)

print(pg.user_exists(213213))

