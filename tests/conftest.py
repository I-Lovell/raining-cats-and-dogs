import pytest, sys, random, py, pytest, os
from xprocess import ProcessStarter
from lib.database_connection import DatabaseConnection
from app import app

# This is a Pytest fixture.
# It creates an object that we can use in our tests.
# We will use it to create a database connection.
@pytest.fixture
def db_connection():
    conn = DatabaseConnection(test_mode=True)
    conn.connect()
    return conn
