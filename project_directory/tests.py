import unittest
from unittest import mock

from project_directory.file_reader import reading_from_csv


class MyTestCase(unittest.TestCase):
    @mock.patch("os.listdir")
    def test_get_files(self, mock_listdir):
        mock_listdir.return_value = ["file1", "file2", "file3"]
        files = reading_from_csv.get_files("sub1/sub2", "data")
        self.assertEqual(3, len(files))


if __name__ == "__main__":
    unittest.main()
