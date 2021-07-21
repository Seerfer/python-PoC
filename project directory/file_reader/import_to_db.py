from .reading_from_csv import default_reader


def db_import(data=default_reader()):
    cities = data[0]
    routes = data[1]
