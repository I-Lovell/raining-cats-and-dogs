# It's Raining Cats and Dogs!

<div style="text-align: center;">
<img title="Cloud Cat" alt="A chubby grey cat representing a cloud" src="static/images/3_overcast.png" width="250" height="250">
</div>

## Description

It's Raining Cats and Dogs is (or will be) a weather app with cat and dog themed weather icons that you can switch between with a toggle. At the moment I'm still working towards the MVP (a weather app with cat themed icons). The icons are taking me a while to draw!

## Tech and Structure

It's Raining Cats and Dogs is a Flask Application. Jinja templates are used to display the forecast data from the API/database on the web page.

The live weather data comes from [Open-Meteo](https://open-meteo.com), a free weather API. Supplementary information (such as the file path to weather icons for each forecast) are stored in a postgresql database.

## Future Features

At the moment I'm still working towards my MVP (a weather website with cat themed weather icons) but my plan for the future of the app is as follows:

- A toggle that allows the user to switch between cat and dog themed icons.
- The ability to choose different cities in the UK to view weather data from (while the app is in development API calls are hardcoded to just call London weather).
- An hourly forecast.
- Secret Bonus Frog themed content???

## Installation

If you'd like to use this as the basis for your own weather website here's what you do

1. Fork this repository
2. Rename the fork
3. Clone the fork to your local machine
4. Create a virtual environment: `python -m venv name_of_venv`
5. Activate your environment: `source name_of_venv/bin/activate`
6. Install the requirements: `pip install -r requirements.txt`
7. Run pytest to check all the tests pass! `pytest`

**Some things to note!**

At the moment the only weather icon you can find in the image folder at the moment is for the overcast cloud cat (which I've included as an example). There are no other weather icons currently available so you'll need to find or make your own. Icons should be about 300x300px.

When you add your icons you'll probably also need to update the SQL seed file to reflect your changes (for example, all the current alt_text stored there talks about cat icons, which you may not have!)

