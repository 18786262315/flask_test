
# from app.extensions import db
from flask import Flask
from config import Config
from werkzeug.utils import import_string
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
blueprints = [
    'app.main.main',
    'app.app01.app01',
    'app.app03.app03',
    'app.app02.app02',
    'app.app04.app04'
]

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    Config.init_app(app)
    # app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    db.init_app(app)
    for bp_name in blueprints:
        bp = import_string(bp_name)
        # print(bp,bp_name)
        app.register_blueprint(bp)
    return app

# db.create_all(app=create_app())

from app import creaters_db




