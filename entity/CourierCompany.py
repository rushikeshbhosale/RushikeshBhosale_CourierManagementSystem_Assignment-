# entity/CourierCompany.py

class CourierCompany:
    def __init__(self, companyName, courierDetails=None, employeeDetails=None, locationDetails=None):
        self.__companyName = companyName
        self.__courierDetails = courierDetails if courierDetails is not None else []
        self.__employeeDetails = employeeDetails if employeeDetails is not None else []
        self.__locationDetails = locationDetails if locationDetails is not None else []

    # Getter methods
    def get_company_name(self):
        return self.__companyName

    def get_courier_details(self):
        return self.__courierDetails

    def get_employee_details(self):
        return self.__employeeDetails

    def get_location_details(self):
        return self.__locationDetails

    # Setter methods
    def set_company_name(self, companyName):
        self.__companyName = companyName

    def set_courier_details(self, courierDetails):
        self.__courierDetails = courierDetails

    def set_employee_details(self, employeeDetails):
        self.__employeeDetails = employeeDetails

    def set_location_details(self, locationDetails):
        self.__locationDetails = locationDetails

    # toString method
    def __str__(self):
        return f"Company Name: {self.__companyName}, " \
               f"Courier Details: {self.__courierDetails}, " \
               f"Employee Details: {self.__employeeDetails}, " \
               f"Location Details: {self.__locationDetails}"
