import os
from typing import NamedTuple

from .csvreader import csv_reader


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


def default_reader():
    return read_files(get_files())
