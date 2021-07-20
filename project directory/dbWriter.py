import flask_sqlalchemy
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = None
db = flask_sqlalchemy.SQLAlchemy()


class Cities(db.Model):
    __tablename__ = "cities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __repr__(self):
        return self.name


class Routes(db.Model):
    __tablename__ = "routes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)
    desc = db.Column(db.String(150))

    def __repr__(self):
        return self.name


def to_json():
    pass
