from lib.forecast import Forecast
from lib.database_connection import DatabaseConnection
from datetime import date
from typing import cast

class ForecastRepository():
    def __init__(self, j_forecast:dict[str, list[str]|list[float]|list[int]], connection:DatabaseConnection):
        self.seven_days: list[Forecast] = []
        self.all_times = cast(list[str], j_forecast['time'])
        self.all_max_temps = cast(list[float], j_forecast['temperature_2m_max'])
        self.all_min_temps = cast(list[float], j_forecast['temperature_2m_min'])
        self.all_weather_codes = cast(list[int], j_forecast['weather_code'])
        self._connection = connection

    # This method takes data from the json response and the database 
    # and creates seven instances of the forecast class, returning them as a list
    # each instance of forecast represents one day, together they make a week!
    def sort_forecast_into_days(self) ->list[Forecast]:
        self.all_times = self.format_date(self.all_times)
        count  = 0
        while count < 7:
            get_code = int(self.all_weather_codes[count])
            weather_detail = self.specify_weather_type(get_code)
            day = Forecast(self.all_times[count], self.all_max_temps[count], self.all_min_temps[count], self.all_weather_codes[count], weather_detail["weather_type"], weather_detail["icon_path"], weather_detail["alt_text"] )
            self.seven_days.append(day)
            count += 1
        return self.seven_days
    
    # This method converts all the date strings in a list into python objects,
    # formats them so they conform to this structure "Tuesday 12 Mar",
    # converts them back into strings and then returns the list 
    def format_date(self, week:list[str]) ->list[str]:
        converted_week = []
        for day in week:
            get_date = date.fromisoformat(day)
            converted_week.append(get_date.strftime("%A %d %b"))
        return converted_week
    
    def specify_weather_type(self, code:int) ->dict[str, str]:
        weather_specifics = self._connection.execute('SELECT weather_type, icon_path, alt_text FROM cat_icons WHERE code = %s', [code])
        # note, our database returns a list with a single dictionary in it,
        # we extract that dictionary and return it
        return weather_specifics[0]

        



        



