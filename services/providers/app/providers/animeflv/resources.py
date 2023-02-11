from urllib.parse import urljoin

from config import ANIMEFLV_BASE_URL
from app.scrapper import get_page


class BaseResource:
    def __init__(self, base_url=ANIMEFLV_BASE_URL, get_resource=get_page):
        self.base_url = base_url
        self.get_resource = get_resource
        self.resource = None

    def _get_url(self, url_path):
        return urljoin(self.base_url, url_path)

    def get(self):
        self.resource = self.get_resource(self.link) if self.link else None

    @property
    def link(self):
        raise NotImplementedError

    def serialize(self):
        pass


class Anime(BaseResource):
    def __init__(self, id=None, title=None, slug=None, score=None):
        self.id = id
        self.title = title
        self._slug = slug
        self._score = score
        self._synopsis = None
        self._prequel = None
        self._sequel = None

        super().__init__()

    def __repr__(self) -> str:
        return f"<Anime (id:{self.id}) {self.title}>"

    @property
    def slug(self):
        if not any([self.title, self._slug]):
            return

        if self._slug:
            return self._slug

        _replace_strings = [(":", ""), ("-", ""), (" ", "-")]
        _title = self.title
        for string in _replace_strings:
            _title = _title.replace(*string)
        self._slug = _title.lower()
        return self._slug

    @property
    def cover(self):
        return (
            self._get_url(f"/uploads/animes/covers/{self.id}.jpg") if self.id else None
        )

    @property
    def thumbnail(self):
        return (
            self._get_url(f"/uploads/animes/thumbs/{self.id}.jpg") if self.id else None
        )

    @property
    def link(self):
        return self._get_url(f"/anime/{self.slug}") if self.slug else None

    @property
    def alternative_title(self):
        if not self._alternative_title:
            self._alternative_title = (
                self.resource.find("span", class_="TxtAlt").text
                if self.resource
                else None
            )
        return self.alternative_title

    @property
    def score(self):
        if not self._score:
            self._score = (
                float(self.resource.find("span", class_="vtprmd").text)
                if self.resource
                else None
            )
        return self._score

    @property
    def synopsis(self):
        if not self._synopsis:
            self._synopsis = (
                self.resource.find("div", class_="Description").text
                if self.resource
                else None
            )
        return self._synopsis

    @property
    def prequel(self):
        if not self._prequel and self.resource:
            _related_target = self.resource.find("ul", class_="ListAnmRel")
            if not _related_target:
                return self._prequel

            _title = [
                r.find("a").text
                for r in _related_target.find_all("li")
                if "precuela" in r.text.lower()
            ][0]
            self._prequel = self.__class__(title=_title)
        return self._prequel

    @property
    def sequel(self):
        if not self._sequel:
            self._sequel = (
                self.__class__(
                    title=[
                        r.find("a").text
                        for r in self.resource.find("ul", class_="ListAnmRel").find_all(
                            "li"
                        )
                        if "secuela" in r.text.lower()
                    ][0]
                )
                if self.resource
                else None
            )
        return self._sequel

    @property
    def episodes(self):
        pass


class Episode(BaseResource):
    def __init__(self, number, link=None, anime: Anime = None):
        self.number = number
        self._link = link
        self.anime = anime

        super().__init__()

    def __repr__(self) -> str:
        return f"<Episode (number:{self.number}) {self.anime}>"

    @property
    def link(self):
        return self._get_url(self._link)
