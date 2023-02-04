import os

from flask import Flask
from flask_migrate import Migrate

from app.extensions import db
from app.routes import animes


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv("APP_SETTINGS", "config.DevelopmentConfig"))
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize Flask extensions here
    db.init_app(app)
    Migrate(app, db)

    # Register blueprints here
    app.register_blueprint(animes.routes)

    return app
