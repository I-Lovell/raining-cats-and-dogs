class Forecast:
    # Initialise weather object using json forecast data
    def __init__(self, forecast):
        self.time = forecast['time']
        self.max_temp = forecast['temperature_2m_max']
        self.min_temp = forecast['temperature_2m_min']
        self.weather_code = forecast['weather_code']
    
    # For comparing two forecast objects
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # Print the forecast object nicely
    def __repr__(self):
        return f"Forecast(time: {self.time}, maximum temperature: {self.max_temp}, minimum temperature: {self.min_temp}, weather codes: {self.weather_code})"