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


class Visit:
    def __init__(self, location, start_time, end_time):
        self.__location = location
        self.__start_time = start_time
        self.__end_time = end_time

    @property
    def location(self):
        return self.__location

    @property
    def start_time(self):
        return self.__start_time

    @property
    def end_time(self):
        return self.__end_time

    def __str__(self) -> str:
        return "Location: " + str(self.__location.latitude) + "\nFrom: " + self.__start_time + " To: " + self.__end_time


class Transition:
    def __init__(self, distance, duration):
        self.__distance = distance
        self.__duration = duration

    @property
    def distance(self):
        return self.__distance

    @property
    def duration(self):
        return self.__duration

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

    def __get_transitions(self, instructions):
        return [Transition(i['distance'], i['duration']) for i in instructions if i['instructionType'] == 'TravelBetweenLocations']

    def __get_visits(self, instructions):
        return [Visit(Location(i['itineraryItem']['name'],
                               i['itineraryItem']['location']['latitude'],
                               i['itineraryItem']['location']['longitude']),
                      i['startTime'], i['endTime']) for i in instructions if i['instructionType'] == 'VisitLocation']

    def compute_route(self):
        requestJSON = {
            'agents' : self.__agents,
            'itineraryItems' : self.__to_visit
        }
        requestJSON = json.dumps(requestJSON)
        headers = {'content-type': 'application/json'}
        response = requests.post(settings.OPTIMIZE_ITINERARY + settings.API_KEY, data=requestJSON, headers=headers)
        itinerary = json.loads(response.text)
        instructions = itinerary['resourceSets'][0]['resources'][0]['agentItineraries'][0]['instructions']
        return self.__get_visits(instructions), self.__get_transitions(instructions)
        #(response.text)