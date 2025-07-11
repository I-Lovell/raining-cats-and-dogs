import os
from flask import Flask, render_template
from lib.forecast_repository import ForecastRepository
from lib.forecast import Forecast
from lib.get_weather import get_weather

# Create flask app (new instance of flask class)
app = Flask(__name__)

# ---------- Routes Start ----------

@app.route('/forecast', methods=['GET'])
def get_basic_forecast():
    data = get_weather()
    repository = ForecastRepository(data)
    week = repository.sort_forecast_into_days()
    return render_template('index.html', week=week)

@app.route('/about', methods=['GET'])
def get_about_page():
    return render_template('about.html')


# ---------- Routes Finish ---------


# Starts server if app.py is run directly
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))