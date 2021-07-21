class Config(object):
    DEBUG = False
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:pass@localhost:5432/baza"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
