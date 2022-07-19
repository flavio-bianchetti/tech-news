import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    headers = {"user-agent": "Fake user-agent"}
    try:
        res = requests.get(url, headers=headers, timeout=3)
        res.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    return res.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    result = list()
    articles = selector.css('div.archive-main > article.entry-preview')
    for article in articles:
        result.append(
            article.css(
                """div.post-inner >
                header.entry-header >
                h2.entry-title >
                a ::attr(href)"""
            ).get()
        )
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css(
        """
        div.nav-links >
        a.next ::attr(href)
        """
    ).get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
