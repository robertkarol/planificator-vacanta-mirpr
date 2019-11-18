class Location:
    def __init__(self, name, latitude, longitude, country=None, city=None, street=None, opening_time='00:00:00', closing_time='23:59:59'):
        """
        Creates a location
        :param name: Desired name for location
        :param latitude: Latitude of location
        :param longitude: Longitude of location
        :param country: Country of location
        :param city: City of location
        :param street: Street of location
        :param opening_time: Opening time of the location (must be "hh:mm:ss" format)
        :param closing_time: Closing time of the location (must be "hh:mm:ss" format)
        """
        self.__name = name
        self.__longitude = longitude
        self.__latitude = latitude
        self.__country = country or ""
        self.__city = city or ""
        self.__street = street or ""
        self.__opening_time = opening_time
        self.__closing_time = closing_time

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

    @property
    def opening_time(self):
        return self.__opening_time

    @property
    def closing_time(self):
        return self.__closing_time

    def __eq__(self, o: object) -> bool:
        if o is not Location: return False
        return self.latitude == o.latitude and self.longitude == o.longitude

    def __ne__(self, o: object) -> bool:
        return not self == o

