import os

basedir = os.path.abspath(os.path.dirname(__file__))

CACHE_PATH = os.path.join(basedir, ".cache")
STATIC_FILES_PATH = os.path.join(basedir, ".static")

# chromedriver
CHROMEDRIVER_PATH = "/home/vnatschke/.local/bin/chromedriver"

# providers settings
ANIMEFLV_BASE_URL = os.getenv("ANIMEFLV_BASE_URL", "https://www3.animeflv.net")
