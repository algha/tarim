from flask import Flask, send_from_directory, current_app
from flask_bcrypt import Bcrypt
from flask_orator import Orator
from flask_login import LoginManager

from app.config import Config
from app.core.algha import Algha

db = Orator()
bcrypt = Bcrypt()
algha = Algha()
login = LoginManager()
login.login_view = "admin.login"

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    env = app.jinja_env
    env.add_extension("app.core.template.PullableExtension")

    db.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)
    algha.init_app(app)

    return app
