from flask import Blueprint
from app.services.animes import AnimeService

routes = Blueprint("animes", __name__, url_prefix="/animes")

@routes.get("/<name>")
def animes(name):
    AnimeService.get_anime(name)
    return f"<p>{name}</p>"
