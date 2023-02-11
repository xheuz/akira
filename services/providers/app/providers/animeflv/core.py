from app.scrapper import get_page
from app.providers.animeflv.resources import Anime, Episode


class AnimeFLV:
    airing_animes = []
    premiere_animes = []
    latest_episodes = []
    latest_animes = []

    def __init__(self, base_url):
        self.base_url = base_url
        self.page = get_page(base_url)

        self.get_latest_episodes()
        self.get_airing_animes()
        self.get_premiere_animes()

    def _get_anime_id(self, url_path):
        return url_path.split("/")[-1].split(".")[0]

    def get_latest_episodes(self):
        # <a class="fa-play" href="/ver/hyouken-no-majutsushi-ga-sekai-wo-suberu-5">
        # <span class="Image"><img alt="Hyouken no Majutsushi ga Sekai wo Suberu" src="/uploads/animes/thumpage/3727.jpg"/></span>
        # <span class="Capi">Episodio 5</span>
        # <strong class="Title">Hyouken no Majutsushi ga Sekai wo Suberu</strong>
        # </a>
        for episode in self.page.find_all("a", class_="fa-play"):
            thumbnail = episode.find("img")["src"]
            anime_id = self._get_anime_id(thumbnail)
            anime_title = episode.find("strong").text

            anime = Anime(id=int(anime_id), title=anime_title)
            self.latest_animes.append(anime)

            link = episode["href"]
            number = episode.find("span", class_="Capi").text.split(" ")[1]
            self.latest_episodes.append(
                Episode(number=int(number), link=link, anime=anime)
            )

    def get_airing_animes(self):
        # <a href="/anime/kyuuketsuki-sugu-shinu-2" class="fa-play-circle">Kyuuketsuki Sugu Shinu 2 <span class="Type tv">Anime</span></a>
        for anime in self.page.find_all("a", class_="fa-play-circle"):
            title = anime.text
            slug = anime["href"].split("/")[-1]
            _type = anime.find("span", class_="Type tv").text
            is_anime = _type.lower() == "anime"

            if not is_anime:
                continue
            self.airing_animes.append(Anime(title=title, slug=slug))

    def get_premiere_animes(self):
        # <article class="Anime alt B">
        # <a href="/anime/majutsushi-orphen-hagure-tabi-urbanramahen">
        # <span class="Estreno"><span>ESTRENO</span></span> <div class="Image fa-play-circle-o">
        # <figure><img src="/uploads/animes/covers/3763.jpg" alt="Majutsushi Orphen Hagure Tabi: Urbanrama-hen"></figure>
        # <span class="Type tv">Anime</span>
        # </div>
        # <h3 class="Title">Majutsushi Orphen Hagure Tabi: Urbanrama-hen</h3>
        # </a>
        # <div class="Description">
        # <div class="Title"><strong>Majutsushi Orphen Hagure Tabi: Urbanrama-hen</strong></div>
        # <p><span class="Type tv">Anime</span> <span class="Vts fa-star">4.1</span></p>
        # <p>Tercera temporada de Majutsushi Orphen Hagure Tabi</p>
        # <a class="Button Vrnmlk" href="/anime/majutsushi-orphen-hagure-tabi-urbanramahen">VER ANIME</a>
        # </div>
        # </article>
        for anime in self.page.find_all("article", class_="Anime alt B"):
            title = anime.find("h3", class_="Title").text
            slug = anime.find("a")["href"].split("/")[-1]
            score = anime.find("span", class_="Vts fa-star").text
            cover = anime.find("img")["src"]
            anime_id = self._get_anime_id(cover)
            _type = anime.find("span", class_="Type tv").text
            is_anime = _type.lower() == "anime"

            if not is_anime:
                continue
            self.premiere_animes.append(
                Anime(id=int(anime_id), title=title, slug=slug, score=float(score))
            )
