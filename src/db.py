import os
from typing import Any
from types import SimpleNamespace as Object

import pandas as pd
import psycopg

DB_URL = os.environ.get("DB_URL")

if DB_URL is None:
    raise Exception("`DB_URL` environment variable not specified.")

def query_single_value(sql: str, args: tuple[str] = None) -> Any:
    """
    Execure the given `sql` with the given `args` and return the single value.
    """
    with psycopg.connect(DB_URL) as con:
        with con.cursor() as cur:
            cur.execute(sql, args)
            return cur.fetchall()[0][0]

def query_single_row(sql: str, args: tuple[str] = None):
    """
    Execure the given `sql` with the given `args` and return a single row.
    """
    with psycopg.connect(DB_URL) as con:
        with con.cursor() as cur:
            cur.execute(sql, args)
            values = {}
            for k, v in zip([column.name for column in cur.description], cur.fetchall()[0]):
                values[k] = v
            return Object(**values)


def query_data_frame(sql: str, args: tuple[str] = None) -> pd.DataFrame:
    """
    Execure the given `sql` with the given `args` and return data as a DataFrame.
    """
    with psycopg.connect(DB_URL) as con:
        with con.cursor() as cur:
            cur.execute(sql, args)
            return pd.DataFrame(cur.fetchall(), columns=[column.name for column in cur.description])



