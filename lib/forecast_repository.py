from lib.forecast import Forecast

class ForecastRepository():
    def __init__(self):
        self.seven_days = []

    # This method takes an instance of the forecast class
    # and sorts all the data into seven dictionaries, each dictionary 
    # representing all the data for a single day
    def sort_forecast_into_days(self, forecast):
        count  = 0
        while count < 7:
            item = {'time': forecast.time[count],'max_temp': forecast.max_temp[count], 'min_temp': forecast.min_temp[count], 'weather_code': forecast.weather_code[count]}
            self.seven_days.append(item)
            count += 1
        return self.seven_days
