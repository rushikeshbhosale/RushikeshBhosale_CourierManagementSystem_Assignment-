#entity/Payment

class Payment:
    def __init__(self, PaymentID, CourierID, LocationID, Amount, PaymentDate):
        self.__PaymentID = PaymentID
        self.__CourierID = CourierID
        self.__LocationID = LocationID
        self.__Amount = Amount
        self.__PaymentDate = PaymentDate

    # Getter methods
    def get_payment_id(self):
        return self.__PaymentID

    def get_courier_id(self):
        return self.__CourierID

    def get_location_id(self):
        return self.__LocationID

    def get_amount(self):
        return self.__Amount

    def get_payment_date(self):
        return self.__PaymentDate

    # Setter methods
    def set_payment_id(self, PaymentID):
        self.__PaymentID = PaymentID

    def set_courier_id(self, CourierID):
        self.__CourierID = CourierID

    def set_location_id(self, LocationID):
        self.__LocationID = LocationID

    def set_amount(self, Amount):
        self.__Amount = Amount

    def set_payment_date(self, PaymentDate):
        self.__PaymentDate = PaymentDate
