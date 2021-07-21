from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from . import config

# Init
app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)


@app.route("/public_transport/city/<name>/routes", methods=["GET"])
def get_route(name):
    pass


@app.route("/public_transport/cities", methods=["GET"])
def get_cities():
    pass


if __name__ == "__main__":
    app.run()
