class Config:
    DEBUG = False
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = "postgresql://user:pass@localhost:5432/baza"
    SQLALCHEMY_TRACK_MODIFICATIONS = False