from animeflv.utils import get_page
from animeflv.settings import BASE_URL


# paths
# episodes: GET /ver/{anime_name}-{episode_number}
# home: GET /anime/{anime_name}


def get_latest_episodes():
    bs = get_page(BASE_URL)
    # <a class="fa-play" href="/ver/hyouken-no-majutsushi-ga-sekai-wo-suberu-5">
    # <span class="Image"><img alt="Hyouken no Majutsushi ga Sekai wo Suberu" src="/uploads/animes/thumbs/3727.jpg"/></span>
    # <span class="Capi">Episodio 5</span>
    # <strong class="Title">Hyouken no Majutsushi ga Sekai wo Suberu</strong>
    # </a>
    for episode in bs.find_all("a", class_="fa-play"):
        url = episode["href"]
        number = episode.find("span", class_="Capi").text
        image = episode.find("img")["src"]
        title = episode.find("strong").text
        print(f"{title} - {number} - {image} -> {url}")


get_latest_episodes()
