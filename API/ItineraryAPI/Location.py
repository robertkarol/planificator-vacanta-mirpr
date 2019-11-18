import dateutil.parser

class Location:
    def __init__(self, name, latitude, longitude, country=None, city=None, street=None, schedule=None):
        """
        Creates a location
        :param name: Desired name for location
        :param latitude: Latitude of location
        :param longitude: Longitude of location
        :param country: Country of location
        :param city: City of location
        :param street: Street of location
        :param schedule: A dictionary with keys being days of the week (like "Wednesday") and values being tuples of hours, such as('00:00:0','23:59:59')
        """
        self.__name = name
        self.__longitude = longitude
        self.__latitude = latitude
        self.__country = country or ""
        self.__city = city or ""
        self.__street = street or ""
        self.__schedule = schedule

    @property
    def name(self):
        return self.__name

    @property
    def longitude(self):
        return self.__longitude

    @property
    def latitude(self):
        return self.__latitude

    @property
    def country(self):
        return self.__country

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    def opening_time(self, date):
        if self.__schedule:
            date = dateutil.parser.parse(date)
            return self.__schedule[date.weekday()][0]
        return '00:00:00'

    def closing_time(self, date):
        if self.__schedule:
            date = dateutil.parser.parse(date)
            return self.__schedule[date.weekday()][1]
        return '23:59:59'

    def __eq__(self, o: object) -> bool:
        if o is not Location: return False
        return self.latitude == o.latitude and self.longitude == o.longitude

    def __ne__(self, o: object) -> bool:
        return not self == o
