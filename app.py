import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template
from lib.forecast_repository import ForecastRepository
from lib.forecast import Forecast
from lib.get_weather import get_weather
from lib.database_connection import DatabaseConnection



# Create flask app (new instance of flask class)
app = Flask(__name__)

# ---------- Routes Start ----------

@app.route('/', methods=['GET'])
def get_basic_forecast() -> str:
    data = get_weather()
    connection = DatabaseConnection() # set this to True when testing or pushing to github
    connection.connect()
    repository = ForecastRepository(data, connection)
    week = repository.sort_forecast_into_days()
    return render_template('index.html', week=week)

@app.route('/about', methods=['GET'])
def get_about_page() -> str:
    return render_template('about.html')


# ---------- Routes Finish ---------


# Starts server if app.py is run directly
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 5001)))