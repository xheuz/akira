from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from undetected_chromedriver import Chrome

from config import CHROMEDRIVER_PATH
from app.scrapper.cache import cache_page


def get_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(executable_path=CHROMEDRIVER_PATH)
    return Chrome(service=service, options=chrome_options)


browser = get_browser()


def get_page(url, skip_cache=False):
    page = None
    if not skip_cache:
        page = cache_page(url)

    if not page:
        browser.get(url)
        page = browser.page_source
        cache_page(url, str(page))
    return BeautifulSoup(page, "lxml")
