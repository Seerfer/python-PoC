import os
import csv
from collections import namedtuple


class csv_reader:
    def __init__(self, name: str, headers_to_read: list) -> None:
        self.file = open(name, "r", encoding="utf-8-sig")
        self.reader = csv.reader(self.file)
        self.name = name
        self.headers = headers_to_read
        self.all_headers = next(self.reader)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        return self.file.close()

    def read_data(self):
        data = namedtuple("data", self.headers)
        return [data(*row) for row in self._list_of_specific_rows()]

    def _list_of_specific_rows(self):
        for row in self.reader:
            yield self.read_specific_elements_of_list(
                row, self.get_indexes_to_read(self.all_headers, self.headers)
            )

    @staticmethod
    def get_indexes_to_read(mainlist, sublist):
        return [mainlist.index(el) for el in sublist]

    @staticmethod
    def read_specific_elements_of_list(mainlist, indexes):
        return [mainlist[i] for i in indexes]

    @property
    def get_name(self):
        _name = self.name.replace(".csv", "")
        return _name.split("/")[-1]
