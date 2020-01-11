from API.ItineraryAPI.Location import Location
from API.ItineraryAPI.TravelItinerary import TravelItinerary
import geocoder

class ServiceRoute:
    def __init__(self):
        pass

    def configureDestionationDetails(self, city):
        self.__city = city

    def configureRouteDetails(self, start_date_time, end_date_time, start_location: Location, end_location: Location = None):
        self.__start_date_time = start_date_time
        self.__end_date_time = end_date_time
        self.__start_location = start_location
        self.__end_location = end_location
        self.__travelItinerary = TravelItinerary(start_date_time, end_date_time, start_location, end_location)

    def getLocationFromCity(self, location_query):
        return Location.get_locations_by_query(location_query, self.__city)

    def getCurrentLocation(self):
        g = geocoder.ip('me')
        return Location('start', g.latlng[0], g.latlng[1])

    def getObjectivesByLocationAndFilter(self, filters):
        pass

    def getFilters(self):
        pass

    def getRouteVisualization(self):
        return self.__map

    def getObjectivesVisitsRoute(self, objectivesVisits):
        for objectivesVisit in objectivesVisits:
            self.__travelItinerary.add_visit(objectivesVisit.location,
                                             objectivesVisit.staying_time,
                                             objectivesVisit.priority)
        visits, tranz, self.__map = self.__travelItinerary.compute_route_and_get_map()

        return visits, tranz