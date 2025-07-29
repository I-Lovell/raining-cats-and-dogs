import pytest, sys, random, py, pytest, os
from xprocess import ProcessStarter
from lib.database_connection import DatabaseConnection
from app import app

# This fixture seeds the database for all our tests in the suite
# seeding once prevents tests from hanging
@pytest.fixture(scope="session")
def seed_test_database():
    conn = DatabaseConnection(test_mode=True)
    conn.connect()
    conn.seed("seeds/weather_icons.sql")
    yield
    with conn.connection.cursor() as cur:
        cur.execute("DROP TABLE cat_icons;")
        cur.execute("DROP SEQUENCE cat_icons_id_seq;")
        conn.connection.commit()


# db_connection depends on seed_test_database 
# (to make sure it doesn't connect to the db before seeding or after teardown logic)
# pass it to all tests that require a db connection/a seeded db
@pytest.fixture
def db_connection(seed_test_database):
    conn = DatabaseConnection(test_mode=True)
    conn.connect()
    return conn

# This fixture starts the test server and makes it available to the tests.
@pytest.fixture
def test_web_address(xprocess):
    python_executable = sys.executable
    app_file = py.path.local(__file__).dirpath("../app.py")
    port = str(random.randint(4100, 4199))
    class Starter(ProcessStarter):
        env = {"PORT": port, "APP_ENV": "test", **os.environ}
        pattern = "Debugger PIN"
        args = [python_executable, app_file]

    xprocess.ensure("flask_test_server", Starter)

    yield f"localhost:{port}"

    xprocess.getinfo("flask_test_server").terminate()


# We'll also create a fixture for the client we'll use to make test requests.
@pytest.fixture
def web_client():
    app.config['TESTING'] = True # This gets us better errors
    with app.test_client() as client:
        yield client
