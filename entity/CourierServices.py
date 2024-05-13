#entity/CourierServices.py

class CourierServices:
    def __init__(self, ServiceID, ServiceName, Cost):
        self.__ServiceID = ServiceID
        self.__ServiceName = ServiceName
        self.__Cost = Cost

    # Getter methods
    def get_service_id(self):
        return self.__ServiceID

    def get_service_name(self):
        return self.__ServiceName

    def get_cost(self):
        return self.__Cost

    # Setter methods
    def set_service_id(self, ServiceID):
        self.__ServiceID = ServiceID

    def set_service_name(self, ServiceName):
        self.__ServiceName = ServiceName

    def set_cost(self, Cost):
        self.__Cost = Cost
