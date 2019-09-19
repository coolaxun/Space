import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard string'
    CSRF_ENABLED = True
    JSON_AS_ASCII = False  # json中的中文格式
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    ADMIN_MAIL_SUBJECT_PREFIX = '[ZX]'
    ADMIN_MAIL_SENDER = 'by admin'
    # 接收邮件的邮箱
    ADMIN_MAIL = os.environ.get('ADMIN_MAIL')

    # cache 缓存
    CACHE_REDIS_TYPE = 'redis'
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = os.getenv('CACHE_REDIS_DB') or ''
    CACHE_REDIS_PASSWORD = os.getenv('CACHE_REDIS_PASSWORD')

    White_list = [
        r'/serve/v1.0/hello',
        r'/api/v1.0/login$',
        r'/api/v1.0/logout/$',
    ]

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/space'
    SQLALCHEMY_DATABASE_URI = os.environ.get('Dev_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'space.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_TEARDOWN = True


class ProductionConfig(Config):
    MAIL_SERVER = os.getenv('MAIL_SERVER') or 'smtp.qq.com'
    MAIL_PORT = os.getenv('MAIL_PORT') or '465'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/space'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 显示提醒a


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}