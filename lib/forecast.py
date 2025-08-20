class Forecast:
    # Initialise weather object using json forecast data
    def __init__(self, time: str, max_temp: float, min_temp: float, weather_code: int, weather_type: str, icon_path: str, alt_text: str) -> None:
        self.time = time
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.weather_code = weather_code
        self.weather_type = weather_type
        self.icon_path = icon_path
        self.alt_text = alt_text
        
    
    # For comparing two forecast objects
    def __eq__(self, other: object) ->bool:
        if not isinstance(other, Forecast):
            return False
        return self.__dict__ == other.__dict__
    
    # Print the forecast object nicely
    def __repr__(self) -> str:
        return f"Forecast(time: {self.time}, maximum temperature: {self.max_temp}, minimum temperature: {self.min_temp}, weather code: {self.weather_code}, weather_type: {self.weather_type}, icon_path: {self.icon_path}, alt_text: {self.alt_text})"