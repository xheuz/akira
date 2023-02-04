from app.extensions import db
from app.models import Base


class Anime(Base):
    __tablename__ = "animes"
    slug = db.Column(db.String(250), unique=True)
    name = db.Column(db.String(250), unique=True)
    name_translation = db.Column(db.String(250), nullable=True)
    episodes = db.Column(db.Integer, nullable=True)
    source = db.Column(db.String(100), nullable=True)
    synopsis = db.Column(db.String(250), nullable=True)
    # rating
    score = db.Column(db.Float(2), nullable=True)
    score_amount_users = db.Column(db.Integer, nullable=True)
    ranked = db.Column(db.Integer, nullable=True)
    # images
    thumbnail = db.Column(db.String(200), nullable=True)
    cover = db.Column(db.String(200), nullable=True)
    # tracking
    last_released = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(200), nullable=True)

    def __repr__(self) -> str:
        return f"<Anime {self.name} (uuid:{self.uuid})>"
