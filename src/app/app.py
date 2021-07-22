from flask import Flask, jsonify

from . import config
from ..file_reader.models import get_class_by_tablename, Cities

# Init
app = Flask(__name__)
app.config.from_object(config.Config)



@app.route("/public_transport/city/<name>/routes", methods=["GET"])
def get_route(name):
    model = get_class_by_tablename(name)
    routes = model.query.all()


@app.route("/public_transport/cities", methods=["GET"])
def get_cities():
    cities = Cities.quert.all()


if __name__ == "__main__":
    app.run()
