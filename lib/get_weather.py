from urllib.request import urlopen
import json

# Get and return weather codes, max and min temperatures 
# and precipitation probability for the next 7 days in London, UK
def get_weather():
    url = urlopen("https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&daily=temperature_2m_max,temperature_2m_min,weather_code&timezone=Europe%2FLondon")
    response = url.read().decode('UTF-8')
    json_data = json.loads(response)
    next_seven_days = json_data['daily']
    return next_seven_days