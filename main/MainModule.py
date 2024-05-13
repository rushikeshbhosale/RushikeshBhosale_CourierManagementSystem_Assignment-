from dao.CourierServiceDB import CourierServiceDb
from entity.Courier import Courier
from entity.Employee import Employee

class MainModule:
    @staticmethod
    def login():
        print('Courier Management System Login')
        print("1. Customer Login")
        print("2. Admin Login")

    @staticmethod
    def user_menu(courier_service):
        print("Courier Management System Customer Menu")
        print("1. Place a new Courier Order")
        print("2. Get Order Status")
        print("3. Cancel a Courier Order")

        option = input("Enter the Operation number: ")
        if option == '1':
            user_id = input("Insert your user id: ")
            sender_name = input("Insert Sender name: ")
            sender_address = input("Insert Sender address: ")
            receiver_name = input("Insert Receiver name: ")
            receiver_address = input("Insert receiver address: ")
            weight = input("Insert weight of the courier: ")
            status = input("Insert courier status: ")
            tracking_number = input("Insert tracking number: ")
            delivery_date = input("Insert delivery date: ")

            courier = Courier(user_id, sender_name, sender_address, receiver_name, receiver_address, weight, status, tracking_number, delivery_date)
            if courier_service.insert_order(courier):
                print("Order Placed successfully.")
            else:
                print("Failed to Place Order")

        elif option == '2':
            tracking_number = input("Insert tracking id of courier: ")
            get_status = courier_service.get_order_status(tracking_number)
            print(get_status)

        elif option == '3':
            tracking_number = input("Insert tracking id to cancel the order: ")
            cancel_order = courier_service.cancel_order(tracking_number)

    @staticmethod
    def admin_menu(courier_service):
        print("Courier Management System Admin Menu")
        print("1. Add an Employee")
        print("2. Update an Employee")
        print("3. Delete an Employee")

        option = input("Enter the Operation Number: ")
        if option == '1':
            employee_name = input("Enter Employee Name: ")
            email = input("Enter E-mail ID: ")
            mobile_number = input("Enter Mobile No.: ")
            role = input("Enter Employee's Role: ")
            salary = input("Enter Employee's Salary: ")
            employee = Employee(employee_name, email, mobile_number, role, salary)
            courier_service.add_employee(employee)
            print("Employee added successfully.")

        elif option == '2':
            employee_id = input("Enter Employee ID to update: ")
            employee_name = input("Enter Updated Employee Name: ")
            email = input("Enter Updated E-mail ID: ")
            mobile_number = input("Enter Updated Mobile No.: ")
            role = input("Enter Updated Employee's Role: ")
            salary = input("Enter Updated Employee's Salary: ")
            employee = Employee(employee_name, email, mobile_number, role, salary, employee_id)
            courier_service.update_employee(employee)

        elif option == '3':
            employee_id = input("Enter Employee ID to delete: ")
            courier_service.delete_employee(employee_id)

    @staticmethod
    def main():
        courier_service = CourierServiceDb()
        while True:
            MainModule.login()
            choice = input('Enter the User type: ')
            if choice == '1':
                MainModule.user_menu(courier_service)
            elif choice == '2':
                MainModule.admin_menu(courier_service)
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    MainModule.main()
