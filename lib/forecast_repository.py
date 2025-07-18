from lib.forecast import Forecast
from datetime import date

class ForecastRepository():
    def __init__(self, j_forecast, connection):
        self.seven_days = []
        self.all_times = j_forecast['time']
        self.all_max_temps = j_forecast['temperature_2m_max']
        self.all_min_temps = j_forecast['temperature_2m_min']
        self.all_weather_codes = j_forecast['weather_code']
        self._connection = connection

    # This method takes an instance of the forecast class
    # and sorts all the data into seven dictionaries, each dictionary 
    # representing all the data for a single day
    def sort_forecast_into_days(self):
        self.all_times = self.format_date(self.all_times)
        count  = 0
        while count < 7:
            get_code = self.all_weather_codes[count]
            weather_detail = self.specify_weather_type(get_code)
            weather_detail = weather_detail[0]
            day = Forecast(self.all_times[count], self.all_max_temps[count], self.all_min_temps[count], self.all_weather_codes[count], weather_detail["weather_type"], weather_detail["icon_path"], weather_detail["alt_text"] )
            self.seven_days.append(day)
            count += 1
        return self.seven_days
    
    # This method converts all the date strings in a list into python objects,
    # formats them so they conform to this structure "Tuesday 12 Mar",
    # converts them back into strings and then returns the list 
    def format_date(self, week):
        converted_week = []
        for day in week:
            day = date.fromisoformat(day)
            converted_week.append(day.strftime("%A %d %b"))
        return converted_week
    
    def specify_weather_type(self, code):
        # note, this returns a list with a single dictionary in it
        weather_specifics = self._connection.execute('SELECT weather_type, icon_path, alt_text FROM cat_icons WHERE code = %s', [code])
        return weather_specifics

        



        



