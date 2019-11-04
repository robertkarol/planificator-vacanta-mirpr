class Location:

    def __init__(self, name, latitude, longitude):
        self.__name = name
        self.__longitude = longitude
        self.__latitude = latitude

class Instruction:
    def __init__(self, start_date_time, end_date_time, start_location, end_location, distance = 0):
        self.__start_date_time = start_date_time
        self.__end_date_time = end_date_time
        self.__start_location = start_location
        self.__end_location = end_location
        self.__distance = distance

    def is_transition(self):
        pass


class TravelItinerary:
    def __init__(self, start_date_time, end_date_time, start_location, end_location = None):
        self.__start_date_time = start_date_time
        self.__end_date_time = end_date_time
        self.__start_location = start_location
        self.__end_location = end_location or start_location
        self.__visits = []

    def add_visit(self, location, date_of_visit, staying_time, priority, opening_time='00:00:00', closing_time='00:00:00'):
        pass

    def compute_route(self):
        pass