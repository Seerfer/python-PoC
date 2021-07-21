import os
from typing import NamedTuple

from csvreader import csv_reader
from models import create_routes_tables, Cities


def get_files(dir: str = "data") -> list:
    data_dir = os.path.join(os.getcwd(), dir)
    files = [
        file
        for file in os.listdir(data_dir)
        if os.path.isfile(os.path.join(data_dir, file))
    ]
    return [os.path.join(data_dir, file) for file in files]


def read_files(files: list) -> (NamedTuple, NamedTuple):
    data = {}
    cities = None
    for f in files:
        with csv_reader(f) as file:
            if file.get_name == "cities":
                cities = file.read_data()
            else:
                data[file.get_name] = file.read_data()

    return cities, data


if __name__ == "__main__":
    cities, data = read_files(get_files())
