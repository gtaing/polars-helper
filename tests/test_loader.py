from unittest import TestCase

from polars_helper.loader import PolarsHelper


class TestPolarsHelper(TestCase):

    def setUp(self):
        self.polars_helper = PolarsHelper()

    def test_load_csv(self):
        df = self.polars_helper.load_csv(path="test_data/input.csv")
        self.assertIsNotNone(df)

    def test_load_parquet(self):
        df = self.polars_helper.load_parquet(path="test_data/input.parquet")
        self.assertIsNotNone(df)

    def test_to_parquet(self):
        csv_file = 'test_data/input.csv'
        destination = 'test_data/new_file.parquet'
        self.polars_helper.to_parquet(csv_file, destination)

        df = self.polars_helper.load_parquet(destination)
        self.assertIsNotNone(df)
