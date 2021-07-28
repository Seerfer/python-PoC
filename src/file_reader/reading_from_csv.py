import os
import re
from typing import Tuple

from file_reader.csvreader import csv_reader
from file_reader.db import import_to_db


def get_files(
    dir_path: str = os.path.abspath(os.path.join(os.getcwd(), os.pardir)),
    dir_name: str = "data",
) -> list:
    full_path = dir_path + "/" + dir_name
    files = [
        file
        for file in os.listdir(full_path)
        if os.path.isfile(os.path.join(full_path, file))
    ]
    return [os.path.join(full_path, file) for file in files]


def _define_headers_to_read(file):
    filename = file.split("/")[-1]
    if re.match("^routes-", filename):
        return ["route_id", "route_short_name", "route_desc"]
    elif re.match("^cities", filename):
        return ["city_id", "city_name"]


def read_files(files: list):
    for f in files:
        headers = _define_headers_to_read(f)
        with csv_reader(f, headers) as file:
            name = file.get_name
            data = file.read_data()
            import_to_db(data, name)


def default_reader():
    return read_files(get_files())
