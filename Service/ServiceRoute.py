from os import listdir

from API.ItineraryAPI.Location import Location
from API.ItineraryAPI.TravelItinerary import TravelItinerary
import geocoder

class ServiceRoute:
    def __init__(self):
        pass

    def configureDestionationDetails(self, city):
        '''
        Usage: this if for when user selected his desired destination and proceeds to planning the route
        :param city:
        :return:
        '''
        self.__city = city

    def configureRouteDetails(self, start_date_time, end_date_time, start_location: Location, end_location: Location = None):
        '''
        Usage: this is for when user is configuring his details for the itinerary (for instance, through a for,
        where he sets these aspects.
        :param start_date_time:
        :param end_date_time:
        :param start_location: this will be retrieved through getLocationFromCity or getCurrentLocation prior to this call
        :param end_location: this will be retrieved through getLocationFromCity or getCurrentLocation prior to this call
        :return:
        '''
        self.__start_date_time = start_date_time
        self.__end_date_time = end_date_time
        self.__start_location = start_location
        self.__end_location = end_location
        self.__travelItinerary = TravelItinerary(start_date_time, end_date_time, start_location, end_location)

    def getLocationFromCity(self, location_query):
        '''
        Usage: this is for when user is s
        :param location_query:
        :return:
        '''
        return Location.get_locations_by_query(location_query, self.__city)

    def getCurrentLocation(self):
        g = geocoder.ip('me')
        return Location('start', g.latlng[0], g.latlng[1])

    def __parseFilterFile(self, filter):
        with open('./' + filter + ".txt") as file:
            for line in file:
                data = line.strip().split(";")
                if len(data[-1]) == 0 or len(data[-2]) == 0:
                    continue
                location = Location(data[0], data[-2], data[-1])

    def getObjectivesByLocationAndFilter(self, filters):
        objectives = []
        for filter in filters:
            objectives.append(self.__parseFilterFile(filter))
        return objectives


    def getFilters(self):
        return [str(file).split(".txt")[0] for file in listdir('./Scrapping/obiectiveData')]

    def getRouteVisualization(self):
        return self.__map

    def getObjectivesVisitsRoute(self, objectivesVisits):
        '''
        Usage: after user gets objectives getObjectivesByLocationAndFilter through and selects his
        preferences (staying time, priority), this method will be used to compute the route
        :param objectivesVisits:
        :return:
        '''
        for objectivesVisit in objectivesVisits:
            self.__travelItinerary.add_visit(objectivesVisit.location,
                                             objectivesVisit.staying_time,
                                             objectivesVisit.priority)
        visits, tranz, self.__map = self.__travelItinerary.compute_route_and_get_map()

        return visits, tranz