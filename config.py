import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    MAIL_SERVER = 'mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USERNAME = '52153418e7c0c0994'
    MAIL_PASSWORD = '61f59fe5bc83e7'
    SVS_MAIL_SUBJECT_PREFIX = '[SVSApp]'
    SVS_MAIL_SENDER = 'SVS_Admin<Svsadmin@svs.com>'
    SVS_ADMIN = 'nirav.joshi05@hotmail.com'
    SVS_PAGE_PHOTO = 10
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    #CELERY_IMPORTS = ("tasks")
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\nirav\\Desktop\\Heroku\\MySVSAppFinal\\SVSdata-dev.db'
    SQLALCHEMY_DATABASE_URI = 'postgres://lttnsfbgpsmzqe:GXff0xU3PXQjtuva3JCzb-66Or@ec2-54-204-41-175.compute-1.amazonaws.com:5432/d7qebl1gu241l2'
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'SVSdata-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'SVSdata.sqlite')

class HerokuConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)
        # handle proxy server headers
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)
        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'default': DevelopmentConfig
}
