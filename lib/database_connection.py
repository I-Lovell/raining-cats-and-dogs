import os
import psycopg
from psycopg.rows import dict_row
from typing import Any


class DatabaseConnection:
    def __init__(self, test_mode: bool=False):
        self._dev = os.getenv("DEV_DATABASE")
        self._test = os.getenv("TEST_DATABASE")
        self.test_mode = test_mode

    def connect(self):
        try:
            if not self.test_mode:
                self.connection = psycopg.connect(dbname = self._dev, row_factory=dict_row)
            else:
                self.connection = psycopg.connect(dbname = self._test, row_factory=dict_row, user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
        except psycopg.OperationalError:
            raise Exception("database connection failed")
    
    def seed(self, sql_file: str):
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_file, "r").read())
            self.connection.commit()

    def execute(self, query: str, params: list[str | int | float | None] | None = None) -> list[dict[str, Any]]:
        if params is None:
            params = []
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        
