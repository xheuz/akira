from pathlib import Path

from animeflv.settings import CACHE_PATH
from animeflv.utils import remove_url_protocol


def read(url):
    path = f"{CACHE_PATH}/{url}"
    if Path(path).is_file():
        print("from cache")
        with open(path, "r") as file:
            return file.read()


def save(url, data):
    path = f"{CACHE_PATH}/{url}"
    with open(path, "w") as file:
        print("saving to cache")
        file.write(data)


def cache_page(url: str, data: str = None) -> str:
    _url = remove_url_protocol(url)
    page = None
    if not data:
        page = read(_url)
    else:
        save(_url, data)
        page = data
    return page
