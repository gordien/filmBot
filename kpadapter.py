import config as cf
import requests
import urlparse
import db


def get_film_info(film_id):
    headers= {
        "accept":"application/json",
        "X-API-KEY" : cf.kinopoisk['secret_key']
    }
    film_info_url = cf.kinopoisk['api_url'] + "films/" + str(film_id)

    film = {}

    try:
        film_info = requests.get(film_info_url, headers =  headers).json()
        film_poster = requests.get(film_info['posterUrlPreview']).content
    except Exception as e:
        return e
    film['external_id'] = film_info['kinopoiskId']
    film['source'] = 'kinopoisk'
    film['description'] = film_info['description'].replace("\xa0", " ").replace("\n"," ")
    film['name'] = film_info['nameRu']
    film['poster_link'] = film_info['posterUrlPreview']
    film['poster_image'] = film_poster
    film['year'] = film_info['year']
    film['duration'] = film_info['filmLength']
    return film


def save_film_info_url(url):
    try:
        return db.save_film_info(get_film_info(urlparse.parse_url(url)))[0]

    except Exception as e:
        print(e)



# print(get_film_info(809))

# print('https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg')

# save_film_info_url('https://www.kinopoisk.ru/series/508161/')