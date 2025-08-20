from lib.forecast import Forecast

"""
Forecast constructs with time, max_temp, min_temp, weather_code, weather_type, icon_path and alt_text
"""
def test_forecast_constructs():
    new_forecast = Forecast('2025-06-04', 18.3, 10.8, 3, "Overcast", "/static/images/3_overcast.png", "A chubby grey cat representing a cloud")
    assert new_forecast.time == '2025-06-04'
    assert new_forecast.max_temp == 18.3
    assert new_forecast.min_temp == 10.8
    assert new_forecast.weather_code == 3
    assert new_forecast.weather_type == "Overcast"
    assert new_forecast.icon_path == "/static/images/3_overcast.png"
    assert new_forecast.alt_text == "A chubby grey cat representing a cloud"

"""
Test Forecast prints to string
"""
def test_forecast_formats_to_string():
    new_forecast = Forecast('2025-06-04', 18.3, 10.8, 3, "Overcast", "/static/images/3_overcast.png", "A chubby grey cat representing a cloud")
    assert str(new_forecast) == "Forecast(time: 2025-06-04, maximum temperature: 18.3, minimum temperature: 10.8, weather code: 3, weather_type: Overcast, icon_path: /static/images/3_overcast.png, alt_text: A chubby grey cat representing a cloud)"

"""
Test two identical forecasts are considered equal
"""
def test_forecasts_are_equal():
    new_forecast_a = Forecast('2025-06-04', 18.3, 10.8, 3, "Overcast", "/static/images/3_overcast.png", "A chubby grey cat representing a cloud")
    new_forecast_b = Forecast('2025-06-04', 18.3, 10.8, 3, "Overcast", "/static/images/3_overcast.png", "A chubby grey cat representing a cloud")
    result = new_forecast_a == new_forecast_b
    assert result == True


"""
Test non-identical forecasts are not considered equal
"""
def test_non_identical_forecast_not_equal():
    new_forecast_a = Forecast('2025-06-04', 18.3, 10.8, 3, "Overcast", "/static/images/3_overcast.png", "A chubby grey cat representing a cloud")
    new_forecast_b = Forecast('2024-08-12', 15.2, 9.8, 61, "Light Rain", "/static/images/61_lightrain.png", "A grumpy grey cat representing a rain cloud with one rain drop")
    result = new_forecast_a == new_forecast_b
    assert result == False

"""
Test no crash occurs when we attempt to compare forecast with a primitive type
"""
def test_equal_check_does_not_break_when_comparing_to_non_forecast():
    new_forecast_a = Forecast('2025-06-04', 18.3, 10.8, 3, "Overcast", "/static/images/3_overcast.png", "A chubby grey cat representing a cloud")
    result = new_forecast_a == 42
    assert result == False