from file_reader.reading_from_csv import default_reader
from file_reader.models import Cities, create_routes_tables


def _import_cities(records: list) -> list:
    to_add = []
    for record in records:
        to_add.append(Cities(record.city_id, record.city_name))
    return to_add


def _create_tables(cities):
    tables = {}
    for city in cities:
        tables[city] = create_routes_tables(city)
    return tables


def _import_routes(cities, routes):
    records = []

    for city in cities:
        table = routes[city]
        for record in cities[city]:
            records.append(
                table(record.route_id, record.route_short_name, record.route_desc)
            )
    return records


def _import(db, records):
    db.create_all()
    db.session.commit()


def db_import(db, data=default_reader()):
    cities, routes = data
    records_to_import = _import_cities(cities)
    route_tables = _create_tables(list(routes.keys()))
    records_to_import.extend(_import_routes(routes, route_tables))
    _import(db, records_to_import)
