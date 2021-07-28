import os
import re
import threading

from file_reader.models import Cities, create_routes_tables, get_class_by_tablename, db
from file_reader.csvreader import csv_reader


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


def import_to_db(data, name, db=db):
    if get_class_by_tablename(name) == None:
        model = create_routes_tables(name)
    model = get_class_by_tablename(name)
    with app.app_context():
        db.create_all()
        records = [model(*record) for record in data]
        db.session.add_all(records)
        db.session.commit()


def read_file(f):
    headers = _define_headers_to_read(f)
    with csv_reader(f, headers) as file:
        name = file.get_name
        data = file.read_data()
        import_to_db(data, name)


def read_files(files: list):
    threads = []
    for f in files:
        t = threading.Thread(target=read_file, args=(f,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


def default_reader(app_parameter):
    global app
    app = app_parameter
    db.reflect()
    return read_files(get_files())
