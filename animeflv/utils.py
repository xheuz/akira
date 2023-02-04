from urllib.parse import urlparse, ParseResult

from bs4 import BeautifulSoup

from animeflv import browser
from animeflv.cache import cache_page


def get_page(url, skip_cache=False):
    page = None
    if not skip_cache:
        page = cache_page(url)

    if not page:
        browser.get(url)
        page = browser.page_source
        cache_page(url, str(page))
    return BeautifulSoup(page, "lxml")


def remove_url_protocol(url):
    _url = urlparse(url)
    return ParseResult("", *_url[1:]).geturl()
