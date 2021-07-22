from flask import Flask

import config
from file_reader.import_to_db import db_import
from file_reader.models import Cities, get_class_by_tablename, db

# Init
app = Flask(__name__)
app.config.from_object(config.Config)
db.init_app(app)
app.app_context().push()



@app.route("/public_transport/city/<name>/routes", methods=["GET"])
def get_route(name):
    model = get_class_by_tablename(name)
    routes = model.query.all()


@app.route("/public_transport/cities", methods=["GET"])
def get_cities():
    cities = Cities.query.all()


if __name__ == "__main__":
    db.create_all()
    db_import(db)

    app.run(port=2137)
