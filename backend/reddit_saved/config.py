import os

class Config(object):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    REDDIT_SECRET = os.environ.get('REDDIT_SECRET')
    REDDIT_ID = os.environ.get('REDDIT_ID')
    SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
    SENDER_EMAIL_PASSWORD = os.environ.get('SENDER_EMAIL_PASSWORD')


class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


if __name__ == "__main__":
    a = DevelopmentConfig()
    print(a.SQLALCHEMY_DATABASE_URI)