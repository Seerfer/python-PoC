from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from . import config

# Init
app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
db.create_all()

@app.route("/public_transport/city/<name>/routes", methods=["GET"])
def get_route(name):
    routes = db.session.query.filetr_by(__tablename__=name).all()


@app.route("/public_transport/cities", methods=["GET"])
def get_cities():
    cities = db.session.query.filetr_by(__tablename__='cities').all()


if __name__ == "__main__":
    app.run()
