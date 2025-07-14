import os
import psycopg


class DatabaseConnection:
    def __init__(self):
        self.dev = os.getenv("DEV_DATABASE")
        self.test = os.getenv("TEST_DATABASE")

    def connect(self, test_mode=False):
        try:
            if not test_mode:
                self.connection = psycopg.connect(self.dev)
            else:
                self.connection = psycopg.connect(self.test)
        except psycopg.OperationalError:
            raise Exception("database connection failed")
    
    def seed(self, sql_file):
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_file, "r").read())
            self.connection.commit
