""" flask_example.py

    Required packages:
    - flask
    - folium

    Usage:

    Start the flask server by running:

        $ python flask_example.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

"""

from flask import Flask
from prepare import geojson_loader
import folium
from folium.plugins import TimestampedGeoJson

app = Flask(__name__)


@app.route('/')
def index():
    a = geojson_loader()

    folium_map = folium.Map(location = [40.71958611647166, -73.9850431174635887],
                        tiles = "CartoDB Positron",
                        zoom_start = 12)


    TimestampedGeoJson(a,
                      period = 'PT1H',
                      duration = 'PT1M',
                      transition_time = 1000,
                      auto_play = True).add_to(folium_map)
    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)