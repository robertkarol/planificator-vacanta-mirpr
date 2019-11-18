from API.ItineraryAPI.TravelItinerary import *

l = [Location("loc1", 46.779792, 23.620796),
     Location("loc2", 46.766435, 23.589105),
     Location("loc3", 46.775976, 23.603794)]
start = Location("start", 46.774775, 23.621636)
ti = TravelItinerary("2019-11-09T08:00:00", "2019-11-09T22:00:00", start, start)

ti.add_visit(l[0], "2019-11-09", "01:00:32.6770000", 1)
ti.add_visit(l[1], "2019-11-09", "02:00:32.6770000", 2)
ti.add_visit(l[2], "2019-11-09", "00:30:32.6770000", 3)

visits, tranz = ti.compute_route()
visits, tranz = ti.compute_route()
visits, tranz = ti.compute_route()
visits, tranz = ti.compute_route()


print("Starting from: ")
print(start.latitude)
print(start.longitude)

for i in range(len(visits)):
    print("\nTransition:")
    print(tranz[i])
    print("\nVisit: ")
    print(visits[i])

print("\nTransition:")
print(tranz[-1])

print("\nEnding at: ")
print(start.latitude)
print(start.longitude)

import wikipedia

# query = query.replace("Wikipedia", " ")
q = "Turda"

try:
    results = wikipedia.summary(q, sentences=4)
except Exception as e:
    print("This search may bring multiple results " + e)
print("According to wikipedia")
print(results)

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Turda",
    "prop": "coordinates"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['pages']

for k, v in PAGES.items():
    print("Latitute: " + str(v['coordinates'][0]['lat']))
    print("Longitude: " + str(v['coordinates'][0]['lon']))