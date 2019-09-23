from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from mongoengine import register_connection

from config import config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    # mongo connect
    con_mongo(config[config_name].mongo_con)

    from .main import main as main_blueprint
    from .serve import serve_blue as serve_1_0_blueprint
    from .auth import auth_blue as auth_blueprint
    from .public import public as public_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(serve_1_0_blueprint, url_prefix='/serve/v1.0')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(public_blueprint, url_prefix='/public/v1.0')

    return app


def con_mongo(con_settings):
    """connect to mongo"""
    for con_dict in con_settings:
        try:
            register_connection(**con_dict)
        except Exception as e:
            print('connect to mongo db error, e=%s' % e)
