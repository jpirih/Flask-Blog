import os


# base config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '=&4\x17o\xa0i\x0b8\xb28e\x89\x1d\xd5\xed-N\xac_\x11\r\x82\x9f'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:student15@localhost/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


# local dev config
class DevConfig(BaseConfig):
    DEBUG = True


# production config
class ProductionCofig(BaseConfig):
    DEBUG = False

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
