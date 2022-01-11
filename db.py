import datetime

import sqlalchemy as db
from sqlalchemy.engine.url import URL
import random


DATABASE = {
    'drivername': 'postgresql',
    'host': 'ec2-52-211-158-144.eu-west-1.compute.amazonaws.com',
    'port': '5432',
    'username': 'rxcpizjqdqetbx',
    'password': '51e1614f079cc5740c2ab06972a57b80e83eb50deb67029e3585eb2f77bfc358',
    'database': 'da4nm97vqnb9ug'
}


def db_create_tables(metadata, engine):
    films = db.Table('films',metadata,
                     db.Column('Id',db.Integer,primary_key=True,autoincrement=True),
                     db.Column('External_id',db.String(255),nullable=False),
                     db.Column('Source',db.String(255),nullable=False),
                     db.Column('Description',db.String),
                     db.Column('Name', db.String,nullable=False),
                     db.Column('poster_link', db.String),
                     db.Column('poster_image', db.LargeBinary),
                     db.Column('year', db.Integer),
                     db.Column('duration', db.Integer),
                     db.Column('deleted', db.Integer),
                     db.UniqueConstraint('External_id','Source', name='unique_film')
                                )
    metadata.create_all(engine)
    return films


def create_connection():
    engine = db.create_engine(URL.create(**DATABASE))
    connection = engine.connect()
    metadata = db.MetaData()
    return engine,connection,metadata


def close_connection(connection,engine):
    connection.close()
    engine.dispose()

def save_film_info(film):
    film_insert = db.insert(films).values(
        External_id = film['external_id'],
        Source = film['source'],
        Description = film['description'],
        Name = film['name'],
        poster_link = film['poster_link'],
        poster_image = film['poster_image'],
        year =  film['year'],
        duration = film['duration'],
        deleted=0
    )
    try:
        result = connection.execute(film_insert)
        return result.inserted_primary_key
    except Exception as e:
        print(e)




def get_film_list():
    select_films = db.select([films.c.Id,films.c.Name,films.c.duration])
    film_list = connection.execute(select_films).where(films.c.deleted == 0).fetchall()
    user_films = "id/название/мин\n"
    for film in film_list:
        film_string = f"{film[0]}) {film[1]}, {film[2]} мин. \n"
        user_films+=film_string
    return user_films

def get_random_film():
    films_id =[]
    select_films = db.select([films.c.Id])
    films_id_from_db = list(connection.execute(select_films).where(films.c.deleted == 0).fetchall())
    for film in films_id_from_db:
        films_id.append(film[0])
    return random.choice(films_id)

def get_film_data(film_id):
    film={}
    select_film_data = db.select([films]).where(films.c.Id == film_id)
    result = connection.execute(select_film_data).fetchone()
    film['id'] = result[0]
    film['external_id'] = result[1]
    film['source'] = result[2]
    film['description'] = result[3]
    film['name'] = result[4]
    film['image'] = result[6]
    film['year'] = result[7]
    film['duration'] = result[8]
    return film

def delete_film(film_id):
    del_film = db.update([films]).where(films.c.Id == film_id).values(deleted=1)
    try:
        connection.execute((del_film))
    except Exception as e:
        print(e)


engine,connection,metadata = create_connection()

films = db_create_tables(metadata,engine)











