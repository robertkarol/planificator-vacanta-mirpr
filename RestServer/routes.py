from flask import Flask
from API.ItineraryAPI.TravelItinerary import *

app = Flask(__name__)


@app.route('/')
def hello_world():

    l = [Location("loc1", 46.779792, 23.620796),
         Location("loc2", 46.766435, 23.589105),
         Location("loc3", 46.775976, 23.603794)]
    start = Location("start", 46.774775, 23.621636)
    ti = TravelItinerary("2019-11-09T08:00:00", "2019-11-09T22:00:00", start, start)

    ti.add_visit(l[0], "2019-11-09", "01:00:32.6770000", 1)
    ti.add_visit(l[1], "2019-11-09", "02:00:32.6770000", 2)
    ti.add_visit(l[2], "2019-11-09", "00:30:32.6770000", 3)

    visits, tranz = ti.compute_route()
    return str(visits[0])