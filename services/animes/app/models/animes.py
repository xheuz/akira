from app.extensions import db
from app.models import Base, GUID


class Anime(Base):
    __tablename__ = "animes"
    slug = db.Column(db.String(250), unique=True)
    title = db.Column(db.String(250), unique=True)
    alternative_titles = db.relationship(
        "AlternativeTitle", backref=db.backref("anime", lazy="select"), lazy="select"
    )
    episodes = db.relationship(
        "Episode", backref=db.backref("anime", lazy="select"), lazy="select"
    )
    synopsis = db.Column(db.String(250), nullable=True)
    # rating
    rating = db.Column(db.String(5), default="U")
    # stats
    score = db.Column(db.Float(2), nullable=True)
    score_by_users = db.Column(db.Integer, nullable=True)
    ranked = db.Column(db.Integer, nullable=True)
    # images
    thumbnail = db.Column(db.String(200), nullable=True)
    cover = db.Column(db.String(200), nullable=True)
    # tracking
    last_released = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(200), nullable=True)
    # categories
    genres = db.relationship(
        "Genre", backref=db.backref("anime", lazy="select"), lazy="select"
    )
    # related
    sequel = db.Column(db.String(), db.ForeignKey("animes.id"), nullable=True)
    # sequel = db.relationship(
    #     "Anime", backref=db.backref("sequel", lazy="select"), lazy="select"
    # )
    prequel = db.Column(db.String(), db.ForeignKey("animes.id"), nullable=True)
    # prequel = db.relationship(
    #     "Anime", backref=db.backref("prequel", lazy="select"), lazy="select"
    # )
    related = db.relationship(
        "RelatedAnime",
        backref=db.backref("anime", lazy="select"),
        lazy="select",
    )

    def __repr__(self) -> str:
        return f"<Anime (id:{self.id}) {self.title}>"


class Genre(Base):
    __tablename__ = "genres"
    anime_id = db.Column(db.String(), db.ForeignKey("animes.id"))
    name = db.Column(db.String())

    def __repr__(self) -> str:
        return f"<Genre (id:{self.id}) {self.name}>"


class AlternativeTitle(Base):
    __tablename__ = "alternative_titles"
    anime_id = db.Column(db.String(), db.ForeignKey("animes.id"))
    language = db.Column(db.String())
    title = db.Column(db.String())

    def __repr__(self) -> str:
        return f"<AlternativeTitle (id:{self.id}) {self.title}>"


class Episode(Base):
    __tablename__ = "episodes"
    anime_id = db.Column(db.String(), db.ForeignKey("animes.id"))
    number = db.Column(db.Integer)
    title = db.Column(db.String(), nullable=True)
    aired_at = db.Column(db.DateTime(), nullable=True)

    def __repr__(self) -> str:
        return f"<Episode (id:{self.id}) {self.title}>"


class RelatedAnime(Base):
    __tablename__ = "related_animes"
    anime_id = db.Column(db.String(), db.ForeignKey("animes.id"))
    to_anime_id = db.Column(db.String(), db.ForeignKey("animes.id"))

    def __repr__(self) -> str:
        return f"<RelatedAnime (id:{self.id}) {self.anime_id} - {self.to_anime_id}>"
