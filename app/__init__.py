from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mongoengine import register_connection

from config import config

db = SQLAlchemy()


def create_app(config_name):
    """create and init a flask app"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    con_mongo(config[config_name].mongo_con)

    register_routes(app)

    app.before_request(handler_request)

    return app


def con_mongo(con_settings):
    """connect to mongo"""
    for con_dict in con_settings:
        try:
            register_connection(**con_dict)
        except Exception as e:
            print('connect to mongo db error, e=%s' % e)


def register_routes(app):
    """register all blueprint to app"""
    from .serve import serve_blue as serve_1_0_blueprint
    from .auth import auth_blue as auth_blueprint
    from .public import public as public_blueprint
    app.register_blueprint(serve_1_0_blueprint, url_prefix='/serve/v1.0')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(public_blueprint, url_prefix='/public/v1.0')


def handler_request():
    pass
