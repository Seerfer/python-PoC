from typing import Tuple

from file_reader.csvreader import csv_reader


def read_files(files: list) -> Tuple:
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
    return read_files(csv_reader.get_files())
