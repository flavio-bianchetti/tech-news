from tech_news.database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
