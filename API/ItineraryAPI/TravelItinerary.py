import json
import requests

from API import settings


class Location:
    def __init__(self, name, latitude, longitude):
        """
        Creates a location
        :param name: Desired name for location
        :param latitude: Latitude of location
        :param longitude: Longitude of location
        """
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
    def __init__(self, location: Location, start_time, end_time):
        """
        Creates a visit for a location
        :param location: Location to be visited
        :param start_time: Start time of the visit (must be "YYYY-MM-DDThh:mm:ss" format)
        :param end_time: End time of the visit (must be "YYYY-MM-DDThh:mm:ss" format)
        """
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
        return "Location: " + str(self.__location.latitude) + " " + str(self.__location.longitude) + "\nFrom: " + self.__start_time + " To: " + self.__end_time


class Transition:
    def __init__(self, distance, duration):
        """
        Creates a transition item
        :param distance: Distance of transition with respect to traffic navigation
        :param duration: Duration of transition with respect to traffic navigation
        """
        self.__distance = distance
        self.__duration = duration

    @property
    def distance(self):
        return self.__distance

    @property
    def duration(self):
        return self.__duration

    def __str__(self) -> str:
        return "Distance: " + str(self.__distance) + "\nDuration: " + self.__duration

class TravelItinerary:
    def __init__(self, start_date_time, end_date_time, start_location: Location, end_location: Location = None):
        """
        Creates a travel itinerary
        :param start_date_time: Start time of the travel (must be "YYYY-MM-DDThh:mm:ss" format)
        :param end_date_time: End time of the travel (must be "YYYY-MM-DDThh:mm:ss" format)
        :param start_location: Location where the travel starts
        :param end_location: Location where the travel ends
        """
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
        self.__modified = True
        self.__cached = None

    def add_visit(self, location: Location, date_of_visit, staying_time, priority, opening_time='00:00:00', closing_time='23:59:59'):
        """
        Adds a visit to a location specifying the details. If opening and closing are not specified, the location is open all the time
        :param location: Location to visit
        :param date_of_visit: Date of the visit (must be "YYYY-MM-DD" format)
        :param staying_time: Staying time of the visit (must be "hh:mm:ss" format)
        :param priority: A priority for scheduling this visit
        :param opening_time: Opening time of the location (must be "hh:mm:ss" format)
        :param closing_time: Closing time of the location (must be "hh:mm:ss" format)
        """
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
        self.__modified = True

    def __get_transitions(self, instructions):
        return [Transition(i['distance'], i['duration']) for i in instructions if i['instructionType'] == 'TravelBetweenLocations']

    def __get_visits(self, instructions):
        return [Visit(Location(i['itineraryItem']['name'],
                               i['itineraryItem']['location']['latitude'],
                               i['itineraryItem']['location']['longitude']),
                      i['startTime'], i['endTime']) for i in instructions if i['instructionType'] == 'VisitLocation']

    def compute_route(self):
        """
        Computes the travel itinerary
        :return: 2 lists: one of visits and one of transitions. At each index in visit, in the corresponding item from transition resides the transition from previous visit to the current one
        """
        if self.__modified and self.__cached == None:
            #print("Server req")
            requestJSON = {
                'agents' : self.__agents,
                'itineraryItems' : self.__to_visit
            }
            requestJSON = json.dumps(requestJSON)
            headers = {'content-type': 'application/json'}
            response = requests.post(settings.OPTIMIZE_ITINERARY + settings.API_KEY, data=requestJSON, headers=headers)
            itinerary = json.loads(response.text)
            self.__cached = itinerary
            self.__modified = False
        else:
            itinerary = self.__cached
        instructions = itinerary['resourceSets'][0]['resources'][0]['agentItineraries'][0]['instructions']
        return self.__get_visits(instructions), self.__get_transitions(instructions)
