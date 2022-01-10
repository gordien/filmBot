import telebot
import sqlalchemy as db
from sqlalchemy.engine.url import URL
from sqlalchemy.sql import exists


DATABASE = {
    'drivername': 'postgresql', #Тут можно использовать MySQL или другой драйвер
    'host': 'ec2-52-211-158-144.eu-west-1.compute.amazonaws.com',
    'port': '5432',
    'username': 'rxcpizjqdqetbx',
    'password': '51e1614f079cc5740c2ab06972a57b80e83eb50deb67029e3585eb2f77bfc358',
    'database': 'da4nm97vqnb9ug'
}

TOKEN = "2110122103:AAERC4s9rn6sRUXFAhNv61Y7aCB5dazMlcQ"

bot = telebot.TeleBot(TOKEN)


def save_user_info(message):
    print(message)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, f"Приветулииии, {message} ")
    save_user_info(message)

@bot.message_handler(commands=['list'])
def get_film_list(message):
    bot.send_message(message.chat.id, "Люблю Печенку")


bot.polling(none_stop=True)


# engine = db.create_engine(URL.create(**DATABASE))
# connection = engine.connect()
# metadata = db.MetaData()
#
#
# users = db.Table('users', metadata,
#               db.Column('Id', db.Integer(),primary_key=True),
#               db.Column('Username', db.String(255), nullable=False)
#               )
#
# metadata.create_all(engine) #Creates the table
#
# query = db.insert(users).values(Id=4, username='naveen')
# ResultProxy = connection.execute(query)
#
# query = db.select([users])
#
# ResultProxy = connection.execute(query)
#
# print(ResultProxy.all())
#
# connection.close()
# engine.dispose()