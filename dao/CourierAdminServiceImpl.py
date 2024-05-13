from dao.ICourierAdminService import ICourierAdminService
from .CourierUserServiceImpl import CourierUserServiceImpl
from entity.CourierCompany import CourierCompany
from entity.Employee import Employee

class CourierAdminServiceImpl(CourierUserServiceImpl, ICourierAdminService):
    def __init__(self, companyObj: CourierCompany):
        super().__init__(companyObj)

    def addCourierStaff(self, name: str, contactNumber: str) -> str:
        # Create a new Employee object with the provided details
        new_employee = Employee(name, contactNumber)
        # Add the new employee to the employee details of the company
        self.companyObj.get_employee_details().append(new_employee)
        return f"New courier staff added successfully. Employee ID: {new_employee.get_employee_id()}"
