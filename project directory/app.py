from flask import Flask, jsonify

# Init
app = Flask(__name__)

import dbWriter


@app.route("/public_transport/city/<name>/routes", methods=["GET"])
def get_route(name):
    pass


@app.route("/public_transport/cities", methods=["GET"])
def get_cities():
    pass
