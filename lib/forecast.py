class Forecast:
    # Initialise weather object using json forecast data
    def __init__(self, time, max_temp, min_temp, weather_code):
        self.time = time
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.weather_code = weather_code
    
    # For comparing two forecast objects
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # Print the forecast object nicely
    def __repr__(self):
        return f"Forecast(time: {self.time}, maximum temperature: {self.max_temp}, minimum temperature: {self.min_temp}, weather codes: {self.weather_code})"