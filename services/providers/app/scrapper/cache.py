from pathlib import Path

from config import CACHE_PATH
from app.scrapper.utils import from_url_to_filename


def read(filename):
    path = f"{CACHE_PATH}/{filename}"
    if Path(path).is_file():
        with open(path, "r") as file:
            return file.read()


def save(filename, data):
    path = f"{CACHE_PATH}/{filename}"
    with open(path, "w") as file:
        file.write(data)


def cache_page(url: str, data: str = None) -> str:
    _filename = from_url_to_filename(url)
    page = None
    if not data:
        page = read(_filename)
    else:
        save(_filename, data)
        page = data
    return page
