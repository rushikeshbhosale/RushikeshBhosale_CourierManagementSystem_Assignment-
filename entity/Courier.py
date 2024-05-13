#entity/Courier.py

class Courier:
    def __init__(self, CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate, Packages):
        self.__CourierID = CourierID
        self.__SenderName = SenderName
        self.__SenderAddress = SenderAddress
        self.__ReceiverName = ReceiverName
        self.__ReceiverAddress = ReceiverAddress
        self.__Weight = Weight
        self.__Status = Status
        self.__TrackingNumber = TrackingNumber
        self.__DeliveryDate = DeliveryDate
        self.__Packages = Packages

    # Getter methods
    def get_courier_id(self):
        return self.__CourierID

    def get_sender_name(self):
        return self.__SenderName

    def get_sender_address(self):
        return self.__SenderAddress

    def get_receiver_name(self):
        return self.__ReceiverName

    def get_receiver_address(self):
        return self.__ReceiverAddress

    def get_weight(self):
        return self.__Weight

    def get_status(self):
        return self.__Status

    def get_tracking_number(self):
        return self.__TrackingNumber

    def get_delivery_date(self):
        return self.__DeliveryDate

    def get_packages(self):
        return self.__Packages

    # Setter methods
    def set_courier_id(self, CourierID):
        self.__CourierID = CourierID

    def set_sender_name(self, SenderName):
        self.__SenderName = SenderName

    def set_sender_address(self, SenderAddress):
        self.__SenderAddress = SenderAddress

    def set_receiver_name(self, ReceiverName):
        self.__ReceiverName = ReceiverName

    def set_receiver_address(self, ReceiverAddress):
        self.__ReceiverAddress = ReceiverAddress

    def set_weight(self, Weight):
        self.__Weight = Weight

    def set_status(self, Status):
        self.__Status = Status

    def set_tracking_number(self, TrackingNumber):
        self.__TrackingNumber = TrackingNumber

    def set_delivery_date(self, DeliveryDate):
        self.__DeliveryDate = DeliveryDate

    def set_packages(self, Packages):
        self.__Packages = Packages
