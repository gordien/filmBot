from urllib.parse import urlparse

sources = {'kp':'www.kinopoisk.ru'}
#переписать - функцию path определять для доругого источника по другому + изменить словарь для источника

def parse_url(url):
    parsed_url = urlparse(url)
    source = parsed_url[1]
    if source in sources.values():
        if source == 'www.kinopoisk.ru':
            film_id = parsed_url[2].split('/')[2]
            return film_id
    else:
        return "Unknown url"
def get_film_id_from_message(message):
    return message.split()[1]

# url = 'https://www.kinopoisk.ru/series/508161/'

# print(parse_url(url))

# print(get_film_id_from_message('Смотреть 11'))