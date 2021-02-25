import os

class Config:
    '''
    General configuration parent class
    '''
    SOURCE_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}' 

    ARTICLE_BASE_URL = 'https://newsapi.org/v2/sources?{}apiKey={}'

    API_KEY = os.environ.get('API_KEY')

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}    