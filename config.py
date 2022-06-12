import os


class Config:
    DEBUG = False
    DEVELOPMENT = False
    DATABASE_URL = os.getenv("DATABASE_URL")


class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
