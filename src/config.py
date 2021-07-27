class Config:
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:pass@localhost:5432/baza"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
