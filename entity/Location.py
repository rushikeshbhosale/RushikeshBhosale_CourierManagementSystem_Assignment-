#entity/Location.py

class Location:
    def __init__(self, LocationID, LocationName, Address):
        self.__LocationID = LocationID
        self.__LocationName = LocationName
        self.__Address = Address

    # Getter methods
    def get_location_id(self):
        return self.__LocationID

    def get_location_name(self):
        return self.__LocationName

    def get_address(self):
        return self.__Address

    # Setter methods
    def set_location_id(self, LocationID):
        self.__LocationID = LocationID

    def set_location_name(self, LocationName):
        self.__LocationName = LocationName

    def set_address(self, Address):
        self.__Address = Address
