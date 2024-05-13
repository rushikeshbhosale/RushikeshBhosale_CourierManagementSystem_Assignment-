#dao/CourierAdminServiceCollectionImpl.py

from dao.ICourierAdminService import ICourierAdminService
from dao.CourierUserServiceCollectionImpl import CourierUserServiceCollectionImpl
from entity.CourierCompanyCollection import CourierCompanyCollection
from entity.Employee import Employee

class CourierAdminServiceCollectionImpl(CourierUserServiceCollectionImpl, ICourierAdminService):
    def __init__(self, companyObj: CourierCompanyCollection):
        super().__init__(companyObj)

    def addCourierStaff(self, name: str, contactNumber: str) -> int:
        # Create a new Employee object with the provided details
        new_employee = Employee(name, contactNumber)
        # Add the new employee to the employee details of the company
        self.companyObj.add_employee(new_employee)
        return new_employee.get_employee_id()
