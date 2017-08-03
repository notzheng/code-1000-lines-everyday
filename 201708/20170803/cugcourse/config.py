import os, sys


class Config:
    SECRET_KEY = 'HuBeiWuHanCUGcourses'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # mail config
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = ''
    MAIL_MAX_EMAILS = None

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:zhengjian0730@localhost/devdb'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:zhengjian0730@localhost/testdb'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:zhengjian0730@localhost/flaskdb'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
