import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET KEY propriamente dia caso não exista'
    DB_USERNAME = os.environ.get('DB_USERNAME') or 'admin'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'admin'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'

class ProductionConfig(Config):
    SEND_FILE_MAX_AGE_DEFAULT = 0,
    SECRET_KEY = os.urandom(16),
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'data-produ.sqlite'),


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': ProductionConfig,
}
    
