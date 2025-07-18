from lib.forecast import Forecast
from lib.forecast_repository import ForecastRepository

# Example JSON forecast data to use in testing 
# (other than forecast1, this is not real data, 
# I just made it up!)
forecast1 = {'time': ['2025-06-04', '2025-06-05', '2025-06-06', '2025-06-07', '2025-06-08', '2025-06-09', '2025-06-10'], 'temperature_2m_max': [18.3, 15.9, 18.2, 16.8, 17.5, 17.8, 20.0], 'temperature_2m_min': [10.8, 13.1, 12.7, 11.3, 9.7, 9.8, 13.3], 'weather_code': [3, 80, 80, 80, 3, 3, 80]}
forecast2 = {'time': ['2025-04-04', '2025-04-05', '2025-04-06', '2025-04-07', '2025-04-08', '2025-04-09', '2025-04-10'], 'temperature_2m_max': [15.1, 13.7, 21.2, 17.9, 13.7, 14.4, 19.2], 'temperature_2m_min': [9.7, 12.8, 10.2, 8.1, 10.5, 7.3, 9.9], 'weather_code': [0, 61, 2, 0, 51, 80, 3]}

"""
Test forecast repository constructs with empty seven_day_forecast
"""
def test_forecast_repo_constructs(db_connection):
    repository = ForecastRepository(forecast1, db_connection)
    assert repository.seven_days == []
    assert repository.all_times == ['2025-06-04', '2025-06-05', '2025-06-06', '2025-06-07', '2025-06-08', '2025-06-09', '2025-06-10']
    assert repository.all_max_temps == [18.3, 15.9, 18.2, 16.8, 17.5, 17.8, 20.0]
    assert repository.all_min_temps == [10.8, 13.1, 12.7, 11.3, 9.7, 9.8, 13.3]
    assert repository.all_weather_codes == [3, 80, 80, 80, 3, 3, 80]

"""
Test forecast Repository sort_forecast_into_days method
corectly sorts 7 days worth of data into a list of seven dictionaries
"""
def test_sort_forecast_into_days(db_connection):
    db_connection.seed("seeds/weather_icons.sql")
    repository = ForecastRepository(forecast2, db_connection)
    formatted_forecast = repository.sort_forecast_into_days()
    assert formatted_forecast == [Forecast('Friday 04 Apr', 15.1, 9.7, 0, "Clear Sky", "/static/images/0_clearsky.png", "A happy cat representing the sun"), Forecast('Saturday 05 Apr', 13.7, 12.8, 61, "Light Rain", "/static/images/61_lightrain.png", "A grumpy grey cat representing a rain cloud with one rain drop"), Forecast('Sunday 06 Apr', 21.2, 10.2, 2, "Partly Cloudy", "/static/images/2_partlycloudy.png", " "), Forecast('Monday 07 Apr', 17.9, 8.1, 0, "Clear Sky", "/static/images/0_clearsky.png", "A happy cat representing the sun"), Forecast('Tuesday 08 Apr', 13.7, 10.5, 51, "Light Drizzle", "/static/images/drizzle.png", " "), Forecast('Wednesday 09 Apr', 14.4, 7.3, 80, "Light Rain Showers", "/static/images/80_lightrainshowers.png", " "), Forecast('Thursday 10 Apr', 19.2, 9.9, 3, "Overcast", "/static/images/3_overcast.png", "A chubby grey cat representing a cloud")]

"""
Test forecast repository format_date method
correctly converts dates into the desired format (example: "Tuesday 12 Mar")
"""
def test_format_date(db_connection):
    repository = ForecastRepository(forecast1, db_connection)
    formatted_dates = repository.format_date(repository.all_times)
    assert formatted_dates == ["Wednesday 04 Jun", "Thursday 05 Jun", "Friday 06 Jun", "Saturday 07 Jun", "Sunday 08 Jun", "Monday 09 Jun", "Tuesday 10 Jun"]

"""
Test forecast repository specify_weather_type method
calls the expected weather_type, icon_path and alt_text based on a weather code
"""
def test_specify_weather_type(db_connection):
    db_connection.seed("seeds/weather_icons.sql") 
    repository = ForecastRepository(forecast1, db_connection)
    result = repository.specify_weather_type(3)
    assert result == [{"weather_type": "Overcast", "icon_path": "/static/images/3_overcast.png", "alt_text": "A chubby grey cat representing a cloud"}]
