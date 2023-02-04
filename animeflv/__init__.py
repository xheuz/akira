from selenium.webdriver.chrome.options import Options
from undetected_chromedriver import Chrome


def get_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return Chrome(options=chrome_options)


browser = get_browser()
