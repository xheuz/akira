import os
import shutil

from urllib.parse import quote, unquote
import requests

from config import STATIC_FILES_PATH


def download_image(url):
    res = requests.get(url, stream=True)
    path = os.path.join(STATIC_FILES_PATH, *url.split("/")[-2:])
    dirname = os.path.dirname(path)
    os.makedirs(dirname)

    if res.status_code == 200:
        with open(path, "wb") as image:
            shutil.copyfileobj(res.raw, image)


def from_url_to_filename(url):
    return quote(url.replace("/", "_"), "")


def from_filename_to_url(string):
    return unquote(string.replace("_", "/"))
