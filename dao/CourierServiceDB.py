from entity import Employee
from util.DBConnUtil import DBConnUtil
from entity.Courier import Courier
from exception.InvalidEmployeeIDException import InvalidEmployeeIDException
from exception.TrackingNumberNotFoundException import TrackingNumberNotFoundException
import mysql.connector
from mysql.connector import Error

class CourierServiceDb:
    connection = DBConnUtil.get_connection()

    @staticmethod
    def insert_order(courier: Courier) -> bool:
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "INSERT INTO Courier (CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate, Packages) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (courier.get_courier_id(), courier.get_sender_name(), courier.get_sender_address(), courier.get_receiver_name(), courier.get_receiver_address(), courier.get_weight(), courier.get_status(), courier.get_tracking_number(), courier.get_delivery_date(), courier.get_packages()))
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
            if not result:
                raise TrackingNumberNotFoundException(tracking_number)
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

    @staticmethod
    def cancel_order(tracking_number):
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "UPDATE Courier SET Status = 'Cancelled' WHERE TrackingNumber = %s"
            cursor.execute(query, (tracking_number,))
            CourierServiceDb.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            if affected_rows == 0:
                raise TrackingNumberNotFoundException(tracking_number)
            else:
                print("Order cancelled successfully.")
        except Error as e:
            print("Error while cancelling order:", e)

    @staticmethod
    def get_assigned_orders(courier_staff_id):
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "SELECT * FROM Courier WHERE AssignedCourierStaffId = %s"
            cursor.execute(query, (courier_staff_id,))
            results = cursor.fetchall()
            cursor.close()
            assigned_orders = []
            for row in results:
                assigned_orders.append({
                    "TrackingNumber": row[7],
                    "SenderName": row[1],
                    "ReceiverName": row[3],
                    "Weight": row[5],
                    "Status": row[6]
                })
            return assigned_orders
        except Error as e:
            print("Error while fetching assigned orders:", e)
            return []

    @staticmethod
    def show_couriers():
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = 'Select * from couriers'
            cursor.execute(query)
            couriers = cursor.fetchall()
            for courier in couriers:
                print(courier)
        except Error as e:
            print("Error while fetching couriers:", e)

    @staticmethod
    def show_employees():
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = 'Select * from employee'
            cursor.execute(query)
            employees = cursor.fetchall()
            for employee in employees:
                print(employee)
        except Error as e:
            print("Error while fetching employees:", e)

    @staticmethod
    def show_users():
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = 'Select * from users'
            cursor.execute(query)
            users = cursor.fetchall()
            for user in users:
                print(user)
        except Error as e:
            print("Error while fetching users:", e)

    @staticmethod
    def add_courier_staff(employee: Employee) -> bool:
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "INSERT INTO Employee (Name, Email, ContactNumber, Role, Salary) VALUES (%s, %s, %s, %s, %s)"
            data = [employee.get_employeename(), employee.get_email(), employee.get_contactnumber(),
                    employee.get_role(), employee.get_salary()]
            cursor.execute(query, data)
            CourierServiceDb.connection.commit()
            cursor.close()
            print("Courier staff added successfully.")
            return True
        except Error as e:
            print("Error adding courier staff:", e)
            return False

    @staticmethod
    def update_employee(employee_id, role):
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = 'Update Employee set Role = %s where employeeid = %s'
            cursor.execute(query, (role, employee_id,))
            CourierServiceDb.connection.commit()
            cursor.close()
            print("Employee role updated successfully.")
        except Error as e:
            print("Error updating employee role:", e)

    @staticmethod
    def delete_employee(employee_id):
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = 'Delete from employee where employeeid = %s'
            cursor.execute(query, (employee_id,))
            CourierServiceDb.connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            if affected_rows == 0:
                raise InvalidEmployeeIDException(employee_id)
            else:
                print("Employee deleted successfully.")
                return True
        except Error as e:
            print("Error deleting employee:", e)
            return False
