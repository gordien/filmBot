import datetime

import sqlalchemy as db
from sqlalchemy.engine.url import URL


DATABASE = {
    'drivername': 'postgresql',
    'host': 'ec2-52-211-158-144.eu-west-1.compute.amazonaws.com',
    'port': '5432',
    'username': 'rxcpizjqdqetbx',
    'password': '51e1614f079cc5740c2ab06972a57b80e83eb50deb67029e3585eb2f77bfc358',
    'database': 'da4nm97vqnb9ug'
}


def db_create_tables(metadata, engine):
    users = db.Table('users', metadata,
                     db.Column('Id', db.Integer(), primary_key=True),
                     db.Column('Username', db.String(255), nullable=False),
                     db.Column('Default_group_id', db.Integer()),
                     )

    user_groups = db.Table('user_groups', metadata,
                     db.Column('Group_id', db.Integer(), primary_key=True),
                     db.Column('Group_name', db.String(255), nullable=False)
                     )

    group_members = db.Table('group_members', metadata,
                     db.Column('Group_id', db.Integer()),
                     db.Column('User_id', db.Integer()),
                    db.UniqueConstraint('Group_id', 'User_id', name='unique_group_member')
                     )

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
                     db.UniqueConstraint('External_id','Source', name='unique_film')
                         )

    user_film_list = db.Table('user_film_list',metadata,
                     db.Column('User_id', db.Integer),
                     db.Column('Group_id', db.Integer),
                     db.Column('Film_id', db.ForeignKey("films.Id")),
                     db.Column('date_add',db.DateTime),
                     db.Column('deleted', db.BOOLEAN)
                        )

    metadata.create_all(engine)
    return users, films, user_film_list, user_groups, group_members


def create_connection():
    engine = db.create_engine(URL.create(**DATABASE))
    connection = engine.connect()
    metadata = db.MetaData()
    return engine,connection,metadata


def close_connection(connection,engine):
    connection.close()
    engine.dispose()


def user_exists(user_id):
    s = users.select()
    return connection.execute(db.select([users]).where(users.c.Id == user_id)).rowcount != 0


def save_user_info(id,username):

    if not user_exists(id):
        user_insert = db.insert(users).values(
            Id = id,
            Username = username
        )
        try:
            connection.execute(user_insert)
        except Exception as e:
                print (e)
    else:
        pass




def save_film_info(film):
    film_insert = db.insert(films).values(
        External_id = film['external_id'],
        Source = film['source'],
        Description = film['description'],
        Name = film['name'],
        poster_link = film['poster_link'],
        poster_image = film['poster_image'],
        year =  film['year'],
        duration = film['duration']
    )
    try:
        result = connection.execute(film_insert)
        return result.inserted_primary_key
    except Exception as e:
        print(e)


def add_film_to_list_db(film_id,user_id):
    film_list_insert = db.insert(user_film_list).values(
        User_id=user_id,
        Film_id=film_id,
        date_add = datetime.datetime.now()
    )
    try:
        connection.execute(film_list_insert)
    except Exception as e:
        print(e)

def get_film_list(user_id):
    pass

engine,connection,metadata = create_connection()

users, films, user_film_list, user_groups, group_members= db_create_tables(metadata,engine)


save_user_info(1,'dasdsa')








