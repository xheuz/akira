from app.models.animes import Anime


class AnimeService:
    @classmethod
    def get_anime(cls, title: str):
        return Anime.query.filter_by(title=title).first()
