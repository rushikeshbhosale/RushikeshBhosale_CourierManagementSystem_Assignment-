#entity/Employee.py

class Employee:
    def __init__(self, EmployeeID, Name, Email, ContactNumber, Role, Salary):
        self.__EmployeeID = EmployeeID
        self.__Name = Name
        self.__Email = Email
        self.__ContactNumber = ContactNumber
        self.__Role = Role
        self.__Salary = Salary

    # Getter methods
    def get_employee_id(self):
        return self.__EmployeeID

    def get_name(self):
        return self.__Name

    def get_email(self):
        return self.__Email

    def get_contact_number(self):
        return self.__ContactNumber

    def get_role(self):
        return self.__Role

    def get_salary(self):
        return self.__Salary

    # Setter methods
    def set_employee_id(self, EmployeeID):
        self.__EmployeeID = EmployeeID

    def set_name(self, Name):
        self.__Name = Name

    def set_email(self, Email):
        self.__Email = Email

    def set_contact_number(self, ContactNumber):
        self.__ContactNumber = ContactNumber

    def set_role(self, Role):
        self.__Role = Role

    def set_salary(self, Salary):
        self.__Salary = Salary
