import os
import json
import polars as pl

from polars import LazyFrame, DataFrame
from typing import Union, Optional


class CsvHelper:

    def read_csv(self, path: str, schema: Optional[dict] = None) -> LazyFrame:

        return pl.scan_csv(path, schema=schema, separator=";", encoding="utf8")

    def write_csv(self, data: Union[DataFrame, LazyFrame], target_path: str):

        if isinstance(data, LazyFrame):
            data.sink_csv(path=target_path, separator=";", include_header=True)

        elif isinstance(data, DataFrame):
            data.write_csv(file=target_path, separator=";", include_header=True)


class ParquetHelper:

    def read_parquet(self, path: str) -> LazyFrame:

        return pl.scan_parquet(path)

    def write_parquet(self, data: Union[DataFrame, LazyFrame], target_path: str):

        if isinstance(data, LazyFrame):
            data.sink_parquet(path=target_path)
        elif isinstance(data, DataFrame):
            data.write_parquet(file=target_path)


class PolarsHelper:

    def __init__(self):
        self.csv_helper = CsvHelper()
        self.parquet_helper = ParquetHelper()

    def load_csv(self, path: str, schema: Optional[dict] = None) -> LazyFrame:

        return self.csv_helper.read_csv(path, schema)

    def load_parquet(self, path: str) -> LazyFrame:

        return self.parquet_helper.read_parquet(path)

    def to_parquet(self, path: str, destination: Optional[str] = None) -> str:

        if destination is None:
            destination = path.split(".csv")[0] + ".parquet"

        df = self.load_csv(path)

        self.parquet_helper.write_parquet(df, destination)

        return destination
