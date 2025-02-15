import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from core.init.cfg import Config
from core.error_handlers import page_not_found

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'user.login'


def create_app():
    app = Flask(__name__, root_path=os.path.abspath("core"))
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    app.register_error_handler(404, page_not_found)

    from core.routers import notes_router, user_router

    app.register_blueprint(notes_router)
    app.register_blueprint(user_router)

    return app