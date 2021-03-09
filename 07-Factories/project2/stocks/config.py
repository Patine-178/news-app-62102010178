import os

class BaseConfig:
    STOCK_API_BASE_URL = "https://financialmodelingprep.com/api/v3/"
    STOCK_API_KEY= os.getenv('STOCK_API_KEY','demo')

class DevConfig(BaseConfig):
    ENV = 'development'

class ProdConfig(BaseConfig):
    ENV = 'production'

configurations = {
    'dev': DevConfig,
    'prod': ProdConfig,
}