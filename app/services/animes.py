from app.models.animes import Anime

class AnimeService:
    @classmethod
    def get_anime(cls, name: str):
        return Anime


