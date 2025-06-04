from lib.forecast import Forecast
from lib.forecast_repository import ForecastRepository

forecast1 = {'time': ['2025-06-04', '2025-06-05', '2025-06-06', '2025-06-07', '2025-06-08', '2025-06-09', '2025-06-10'], 'temperature_2m_max': [18.3, 15.9, 18.2, 16.8, 17.5, 17.8, 20.0], 'temperature_2m_min': [10.8, 13.1, 12.7, 11.3, 9.7, 9.8, 13.3], 'weather_code': [3, 80, 80, 80, 3, 3, 80]}

"""
Test forecast repository constructs with empty seven_day_forecast
"""
def test_forecast_repo_constructs():
    repository = ForecastRepository()
    assert repository.seven_days == []

"""
Test forecast Repository sort_forecast_into_days method
corectly sorts 7 days worth of data into a list of seven dictionaries
"""
def test_sort_forecast_into_days():
    repository = ForecastRepository()
    new_forecast = Forecast(forecast1)
    formatted_forecast = repository.sort_forecast_into_days(new_forecast)
    assert formatted_forecast == [{'time':'2025-06-04', 'max_temp': 18.3, 'min_temp': 10.8, 'weather_code': 3}, {'time': '2025-06-05','max_temp': 15.9, 'min_temp': 13.1,'weather_code': 80}, {'time': '2025-06-06','max_temp': 18.2, 'min_temp': 12.7,'weather_code': 80}, {'time': '2025-06-07','max_temp': 16.8, 'min_temp': 11.3,'weather_code': 80}, {'time': '2025-06-08','max_temp': 17.5, 'min_temp': 9.7,'weather_code': 3}, {'time': '2025-06-09','max_temp': 17.8, 'min_temp': 9.8,'weather_code': 3}, {'time': '2025-06-10','max_temp': 20.0, 'min_temp': 13.3,'weather_code': 80}]