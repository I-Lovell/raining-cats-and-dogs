from lib.database_connection import DatabaseConnection

"""
DatabaseConnection class can seed weather data 
and retrieve it with a weather code
"""

def test_database_connection_seed_and_retrieve_with_code():
    connection = DatabaseConnection(test_mode=True)
    connection.connect()
    connection.seed("seeds/weather_icons.sql")
    result = connection.execute("SELECT * FROM cat_icons WHERE code=3")
    assert result == [{"id": 4, "code": 3, "weather_type": "Overcast", "icon_path": "/static/images/3_overcast.png", "alt_text": "A chubby grey cat representing a cloud"}]
