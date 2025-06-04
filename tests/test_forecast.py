from lib.forecast import Forecast

# Example JSON forecast data to use in testing 
# (other than forecast1, this is not real data, 
# I just made it up!)
forecast1 = {'time': ['2025-06-04', '2025-06-05', '2025-06-06', '2025-06-07', '2025-06-08', '2025-06-09', '2025-06-10'], 'temperature_2m_max': [18.3, 15.9, 18.2, 16.8, 17.5, 17.8, 20.0], 'temperature_2m_min': [10.8, 13.1, 12.7, 11.3, 9.7, 9.8, 13.3], 'weather_code': [3, 80, 80, 80, 3, 3, 80]}
forecast2 = {'time': ['2025-04-04', '2025-04-05', '2025-04-06', '2025-04-07', '2025-04-08', '2025-04-09', '2025-04-10'], 'temperature_2m_max': [15.1, 13.7, 21.2, 17.9, 13.7, 14.4, 19.2], 'temperature_2m_min': [9.7, 12.8, 10.2, 8.1, 10.5, 7.3, 9.9], 'weather_code': [0, 61, 2, 0, 51, 80, 3]}

"""
Forecast constructs with time, max_temp, min_temp and weather_code
"""
def test_forecast_constructs():
    new_forecast = Forecast(forecast1)
    assert new_forecast.time == ['2025-06-04', '2025-06-05', '2025-06-06', '2025-06-07', '2025-06-08', '2025-06-09', '2025-06-10']
    assert new_forecast.max_temp == [18.3, 15.9, 18.2, 16.8, 17.5, 17.8, 20.0]
    assert new_forecast.min_temp == [10.8, 13.1, 12.7, 11.3, 9.7, 9.8, 13.3]
    assert new_forecast.weather_code == [3, 80, 80, 80, 3, 3, 80]

"""
Test forcast prints to string
"""
def test_forecast_formats_to_string():
    new_forecast = Forecast(forecast2)
    assert str(new_forecast) == "Forecast(time: ['2025-04-04', '2025-04-05', '2025-04-06', '2025-04-07', '2025-04-08', '2025-04-09', '2025-04-10'], maximum temperature: [15.1, 13.7, 21.2, 17.9, 13.7, 14.4, 19.2], minimum temperature: [9.7, 12.8, 10.2, 8.1, 10.5, 7.3, 9.9], weather codes: [0, 61, 2, 0, 51, 80, 3])"

"""
Test two identical forecasts are considered equal!
"""
def test_forecasts_are_equal():
    new_forecast_a = Forecast(forecast1)
    new_forecast_b = Forecast(forecast1)
    assert new_forecast_a == new_forecast_b