from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    result = list()
    search = search_news({
        'title': {
            # https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison
            '$regex': f'{title.casefold()}',
        }
    })

    for item in search:
        result.append((item['title'], item['url']))

    return result


# Requisito 7
def search_by_date(date):
    try:
        result = list()
        search_date = datetime.strptime(date, '%Y-%m-%d')
        if type(search_date) is not datetime:
            raise ValueError
        search = search_news({
            # https://www.geeksforgeeks.org/python-reversed-split-strings/
            "timestamp":  "/".join(reversed(date.split('-'))),
        })
        for item in search:
            result.append((item['title'], item['url']))
        return result
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
