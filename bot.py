import telebot


TOKEN = "2110122103:AAERC4s9rn6sRUXFAhNv61Y7aCB5dazMlcQ"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, "Приветулииии")

@bot.message_handler(commands=['list'])
def get_film_list(message):
    bot.send_message(message.chat.id, "Список фильмов будет тут")


bot.polling(none_stop=True)
