# dao/CourierAdminServiceCollectionImpl.py

from dao.ICourierAdminService import ICourierAdminService
from dao.CourierUserServiceCollectionImpl import CourierUserServiceCollectionImpl
from entity.CourierCompanyCollection import CourierCompanyCollection
from entity.Employee import Employee


class CourierAdminServiceCollectionImpl(CourierUserServiceCollectionImpl, ICourierAdminService):
    def __init__(self, companyObj: CourierCompanyCollection):
        super().__init__(companyObj)

    def add_courier_staff(self, name: str, contactNumber: str) -> int:
        # Create a new Employee object with the provided details
        new_employee = Employee(name, contactNumber)
        # Add the new employee to the employee details of the company
        self.companyObj.add_employee(new_employee)
        return new_employee.get_employee_id()


# dao/CourierAdminServiceImpl.py

from dao.ICourierAdminService import ICourierAdminService
from dao.CourierUserServiceImpl import CourierUserServiceImpl
from entity.CourierCompany import CourierCompany
from entity.Employee import Employee


class CourierAdminServiceImpl(CourierUserServiceImpl, ICourierAdminService):
    def __init__(self, companyObj: CourierCompany):
        super().__init__(companyObj)

    def add_courier_staff(self, name: str, contactNumber: str) -> str:
        # Create a new Employee object with the provided details
        new_employee = Employee(name, contactNumber)
        # Add the new employee to the employee details of the company
        self.companyObj.get_employee_details().append(new_employee)
        return f"New courier staff added successfully. Employee ID: {new_employee.get_employee_id()}"


# dao/CourierServiceDb

from util.DBConnUtil import DBConnUtil
from entity.Courier import Courier
import mysql.connector
from mysql.connector import Error


class CourierServiceDb:
    connection = DBConnUtil.get_connection()

    @staticmethod
    def insert_order(courier: Courier) -> bool:
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "INSERT INTO Courier (CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate, Packages) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (courier.get_courier_id(), courier.get_sender_name(), courier.get_sender_address(),
                                   courier.get_receiver_name(), courier.get_receiver_address(), courier.get_weight(),
                                   courier.get_status(), courier.get_tracking_number(), courier.get_delivery_date(),
                                   courier.get_packages()))
            CourierServiceDb.connection.commit()
            cursor.close()
            print("Order inserted successfully.")
            return True
        except Error as e:
            print("Error inserting order:", e)
            return False

    @staticmethod
    def update_courier_status(tracking_number: str, new_status: str) -> bool:
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "UPDATE Courier SET Status = %s WHERE TrackingNumber = %s"
            cursor.execute(query, (new_status, tracking_number))
            CourierServiceDb.connection.commit()
            cursor.close()
            print("Courier status updated successfully.")
            return True
        except Error as e:
            print("Error updating courier status:", e)
            return False

    @staticmethod
    def retrieve_delivery_history(tracking_number: str) -> list:
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "SELECT * FROM Courier WHERE TrackingNumber = %s"
            cursor.execute(query, (tracking_number,))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print("Error retrieving delivery history:", e)
            return []

    @staticmethod
    def generate_shipment_status_report() -> list:
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "SELECT TrackingNumber, Status FROM Courier"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print("Error generating shipment status report:", e)
            return []

    @staticmethod
    def generate_revenue_report() -> list:
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "SELECT TrackingNumber, Status FROM Courier WHERE Status = 'Delivered'"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print("Error generating revenue report:", e)
            return []


# dao/CourierUserServiceCollectionImpl.py

from dao.ICourierUserService import ICourierUserService
from entity.CourierCompanyCollection import CourierCompanyCollection
from entity.Courier import Courier


class CourierUserServiceCollectionImpl(ICourierUserService):
    def __init__(self, company_obj: CourierCompanyCollection):
        self.company_obj = company_obj

    def insert_order(self, courier: Courier) -> bool:
        self.company_obj.courier_details.append(courier)
        print("Order placed successfully.")

    def get_order_status(self, tracking_number):
        for courier in self.company_obj.courier_details:
            if courier.get_tracking_number() == tracking_number:
                return courier.get_status()
        return "Order not found"

    def cancel_order(self, tracking_number):
        for courier in self.company_obj.courier_details:
            if courier.get_tracking_number() == tracking_number:
                courier.set_status("Cancelled")
                print("Order cancelled successfully.")
                return
        print("Order not found")

    def get_assigned_orders(self, courier_staff_id):
        assigned_orders = []
        for courier in self.company_obj.courier_details:
            if courier.get_assigned_courier_staff_id() == courier_staff_id:
                assigned_orders.append(courier)
        return assigned_orders


# dao/CourierUserServiceImpl

from dao.ICourierUserService import ICourierUserService
from entity.Courier import Courier
from entity.CourierCompany import CourierCompany


class CourierUserServiceImpl(ICourierUserService):
    def __init__(self, companyObj: CourierCompany):
        self.companyObj = companyObj

    def placeOrder(self, courierObj: Courier) -> str:
        # Add the courier to the courier details of the company
        self.companyObj.get_courier_details().append(courierObj)
        return f"Order placed successfully. Tracking Number: {courierObj.get_tracking_number()}"

    def getOrderStatus(self, trackingNumber: str) -> str:
        for courier in self.companyObj.get_courier_details():
            if courier.get_tracking_number() == trackingNumber:
                return f"Order Status: {courier.get_status()}"
        return "Order not found"

    def cancelOrder(self, trackingNumber: str) -> str:
        for courier in self.companyObj.get_courier_details():
            if courier.get_tracking_number() == trackingNumber:
                courier.set_status("Cancelled")
                return "Order cancelled successfully."
        return "Order not found"

    def getAssignedOrder(self, courierStaffId: str) -> list:
        assigned_orders = []
        for courier in self.companyObj.get_courier_details():
            if courier.get_assigned_courier_staff_id() == courierStaffId:
                assigned_orders.append(courier)
        return assigned_orders


# dao/ICourierAdminService.py

from abc import ABC, abstractmethod
from entity.Employee import Employee
from dao.ICourierUserService import ICourierUserService


class ICourierAdminService(ICourierUserService):
    @abstractmethod
    def addCourierStaff(self, name, contactNumber):
        pass


# dao/ICourierUserService.py

from abc import ABC, abstractmethod
from entity.Courier import Courier


class ICourierUserService(ABC):
    @abstractmethod
    def placeOrder(self, courierObj):
        pass

    @abstractmethod
    def getOrderStatus(self, trackingNumber):
        pass

    @abstractmethod
    def cancelOrder(self, trackingNumber):
        pass

    @abstractmethod
    def getAssignedOrder(self, courierStaffId):
        pass


# Fetch data implementation
def fetch_data():
    try:
        # Placeholder for fetching data from the database
        data = fetch_data_from_database()

        # Placeholder for processing fetched data
        process_data(data)

    except Exception as e:
        print("Error fetching data:", e)


def fetch_data_from_database():
    # Placeholder for fetching data from the database
    return [("John Doe", "johndoe@example.com"), ("Jane Smith", "janesmith@example.com")]


def process_data(data):
    # Placeholder for processing fetched data
    for row in data:
        print(row)


# Call fetch_data function
fetch_data()
