import csv
from collections import namedtuple


class csv_reader:
    def __init__(self, name: str) -> None:
        self.file = open(name, "r")
        self.reader = csv.reader(self.file)

    def __enter__(self):
        return self

    def __exit__(self):
        return self.file.close()

    @staticmethod
    def read_columns(reader):
        return namedtuple("data", next(reader))

    def read_data(self):
        data = self.read_columns(self.reader)
        return [data(*row) for row in self.reader]
