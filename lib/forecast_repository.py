from lib.forecast import Forecast

class ForecastRepository():
    def __init__(self, j_forecast):
        self.seven_days = []
        self.all_times = j_forecast['time']
        self.all_max_temps = j_forecast['temperature_2m_max']
        self.all_min_temps = j_forecast['temperature_2m_min']
        self.all_weather_codes = j_forecast['weather_code']

    # This method takes an instance of the forecast class
    # and sorts all the data into seven dictionaries, each dictionary 
    # representing all the data for a single day
    def sort_forecast_into_days(self):
        count  = 0
        while count < 7:
            day = Forecast(self.all_times[count], self.all_max_temps[count], self.all_min_temps[count], self.all_weather_codes[count])
            self.seven_days.append(day)
            count += 1
        return self.seven_days
