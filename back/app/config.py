from dotenv import load_dotenv
import os
load_dotenv()


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '7soino32noonN@^#iuiuw9'

    PSQL_CONFIG = {
        'production': {
            'PSQL_SERVER': os.getenv('PROD_PSQL_SERVER'),
            'PSQL_PORT': os.getenv('PROD_PSQL_PORT'),
            'PSQL_DB': os.getenv('PROD_PSQL_DB'),
            'PSQL_USERNAME': os.getenv('PROD_PSQL_USERNAME'),
            'PSQL_PASSWORD': os.getenv('PROD_PSQL_PASSWORD'),
        },
        'development': {
            'PSQL_SERVER': os.environ.get('DEV_PSQL_SERVER'),
            'PSQL_PORT': os.environ.get('DEV_PSQL_PORT'),
            'PSQL_DB': os.environ.get('DEV_PSQL_DB'),
            'PSQL_USERNAME': os.environ.get('DEV_PSQL_USERNAME'),
            'PSQL_PASSWORD': os.environ.get('DEV_PSQL_PASSWORD'),
        },
        'testing': {
            'PSQL_SERVER': os.environ.get('TEST_PSQL_SERVER'),
            'PSQL_PORT': os.environ.get('TEST_PSQL_PORT'),
            'PSQL_DB': os.environ.get('TEST_PSQL_DB'),
            'PSQL_USERNAME': os.environ.get('TEST_PSQL_USERNAME'),
            'PSQL_PASSWORD': os.environ.get('TEST_PSQL_PASSWORD'),
        }
    }

    RATE_LIMITER_OPTS = ['200 per day', '50 per hour']
    ADMINS = ['admin@gmail.com']
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

    @staticmethod
    def init_app(app):
        pass

    def get_psql_uri(self, config_name):
        configValue = self.PSQL_CONFIG.get(config_name)
        if configValue:
            return f'postgresql://{configValue["PSQL_USERNAME"]}:{configValue["PSQL_PASSWORD"]}@{configValue["PSQL_SERVER"]}:{configValue["PSQL_PORT"]}/{configValue["PSQL_DB"]}'
        else:
            return None


class ProductionConfig(Config):
    PSQL_URI = Config().get_psql_uri('production')


class DevelopmentConfig(Config):
    DEBUG = True
    PSQL_URI = Config().get_psql_uri('development')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    PSQL_URI = Config().get_psql_uri('testing')


config = {
    'base': Config,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
