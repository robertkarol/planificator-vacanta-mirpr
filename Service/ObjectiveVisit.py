from API.ItineraryAPI.Location import Location


class ObjectiveVisit:
    def __init__(self, location: Location, staying_time, priority):
        self.location = location
        self.staying_time = staying_time
        self.priority = priority