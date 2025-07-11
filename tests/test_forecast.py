from lib.forecast import Forecast

"""
Forecast constructs with time, max_temp, min_temp and weather_code
"""
def test_forecast_constructs():
    new_forecast = Forecast('2025-06-04', 18.3, 10.8, 3)
    assert new_forecast.time == '2025-06-04'
    assert new_forecast.max_temp == 18.3
    assert new_forecast.min_temp == 10.8
    assert new_forecast.weather_code == 3

"""
Test Forecast prints to string
"""
def test_forecast_formats_to_string():
    new_forecast = Forecast('2025-06-04', 18.3, 10.8, 3)
    assert str(new_forecast) == "Forecast(time: 2025-06-04, maximum temperature: 18.3, minimum temperature: 10.8, weather code: 3)"

"""
Test two identical forecasts are considered equal!
"""
def test_forecasts_are_equal():
    new_forecast_a = Forecast('2025-06-04', 18.3, 10.8, 3)
    new_forecast_b = Forecast('2025-06-04', 18.3, 10.8, 3)
    assert new_forecast_a == new_forecast_b