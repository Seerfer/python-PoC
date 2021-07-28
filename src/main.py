from flask import Flask, jsonify

import config
from file_reader.models import Cities, get_class_by_tablename, db
from file_reader.csv_to_db import default_reader


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)
    db.init_app(app)
    app.app_context().push()
    return app


if __name__ == "__main__":
    app = create_app()
    default_reader(app)
    app.run(use_reloader=False)


@app.route("/public_transport/city/<name>/routes", methods=["GET"])
def get_route(name):
    model = get_class_by_tablename(name)
    routes = model.query.all()
    return jsonify(json_list=[i.serialize() for i in routes])


@app.route("/public_transport/cities", methods=["GET"])
def get_cities():
    cities = Cities.query.all()
    return jsonify(json_list=[i.serialize() for i in cities])
