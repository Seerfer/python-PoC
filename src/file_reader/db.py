from file_reader.models import Cities, create_routes_tables, get_class_by_tablename, db


def import_to_db(data, name, db=db):
    print(data)
    if get_class_by_tablename(name) == None:
        model = create_routes_tables(name)
    model = get_class_by_tablename(name)
