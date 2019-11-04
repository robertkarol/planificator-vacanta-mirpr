import json
import requests

from Lab1.src import settings


class Location:

    def __init__(self, name, latitude, longitude):
        self.__name = name
        self.__longitude = longitude
        self.__latitude = latitude

    @property
    def name(self):
        return self.__name

    @property
    def longitude(self):
        return self.__longitude

    @property
    def latitude(self):
        return self.__latitude

    def __eq__(self, o: object) -> bool:
        if o is not Location: return False
        return self.latitude == o.latitude and self.longitude == o.longitude

    def __ne__(self, o: object) -> bool:
        return not self == o


class Instruction:
    def __init__(self, start_date_time, end_date_time, start_location, end_location, distance = 0):
        self.__start_date_time = start_date_time
        self.__end_date_time = end_date_time
        self.__start_location = start_location
        self.__end_location = end_location
        self.__distance = distance

    def is_transition(self):
        return self.__distance == 0 and self.__start_location != self.__end_location


class TravelItinerary:
    def __init__(self, start_date_time, end_date_time, start_location, end_location = None):
        self.__start_date_time = start_date_time
        self.__end_date_time = end_date_time
        self.__start_location = start_location
        self.__end_location = end_location or start_location
        self.__visits = []
        self.__to_visit = []
        self.__agents = [{
            'name' : 'travelPlanner',
            "shifts": [
                {
                    "startTime": start_date_time,
                    "startLocation": {
                        "latitude": self.__start_location.latitude,
                        "longitude": self.__start_location.longitude
                    },
                    "endTime": end_date_time,
                    "endLocation": {
                        "latitude": self.__end_location.latitude,
                        "longitude": self.__end_location.longitude
                    }
                }
            ]
        }]

    def add_visit(self, location, date_of_visit, staying_time, priority, opening_time='00:00:00', closing_time='23:59:59'):
        visit = {
            "name": location.name,
            "OpeningTime": date_of_visit + 'T' + opening_time,
            "ClosingTime": date_of_visit + 'T' + closing_time,
            "DwellTime": staying_time,
            "Priority": int(priority),
            "Location": {
                "Latitude": location.latitude,
                "Longitude": location.longitude
            }
        }
        self.__to_visit.append(visit)

    def compute_route(self):
        requestJSON = {
            'agents' : self.__agents,
            'itineraryItems' : self.__to_visit
        }
        requestJSON = json.dumps(requestJSON)
        headers = {'content-type': 'application/json'}
        response = requests.post(settings.OPTIMIZE_ITINERARY + settings.API_KEY, data=requestJSON, headers=headers)
        print(response.text)