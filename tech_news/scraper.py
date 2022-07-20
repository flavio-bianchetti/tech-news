import requests
import time
from parsel import Selector
# https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
import re


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
    selector = Selector(html_content)

    comments_count = selector.css(
        'div.post-comments h5.title-block ::text'
    ).get()
    if comments_count is None:
        comments_count = 0
    else:
        comments_count = int(re.search(r'\d+', comments_count).group())

    result = {
        'url': selector.css('link[rel="canonical"]::attr(href)').get(),
        'title': (selector.css(
            'div.entry-header-inner h1.entry-title ::text'
        ).get()).strip(),
        'timestamp': selector.css('ul.post-meta > li.meta-date ::text').get(),
        'writer': selector.css('span.author a.url ::text').get(),
        'comments_count': comments_count,
        'summary': "".join(selector.css(
            'div.entry-content > p:nth-of-type(1) *::text'
        ).getall()).strip(),
        'tags': selector.css(
            'section.post-tags ul li:not(:first-child) ::text'
        ).getall(),
        'category': selector.css(
            'div.meta-category a.category-style span.label ::text'
        ).get(),
    }
    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
