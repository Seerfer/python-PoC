import csv
from collections import namedtuple


class csv_reader:
    def __init__(self, name: str) -> None:
        self.file = open(name, "r", encoding="utf-8-sig")
        self.reader = csv.reader(self.file)
        self.name = name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        return self.file.close()

    @staticmethod
    def _read_columns(reader):
        return namedtuple("data", next(reader))

    def read_data(self):
        data = self._read_columns(self.reader)
        return [data(*row) for row in self.reader]

    @property
    def get_name(self):
        _name = self.name.replace("routes-", "")
        _name = _name.replace(".csv", "")
        return _name.split("/")[-1]
