from dao.CourierServiceDB import CourierServiceDb
from entity.Courier import Courier
from entity.Employee import Employee
from entity.User import User


class MainModule:
    @staticmethod
    def login():
        print('Courier Management System Login')
        print("1. Customer Login")
        print("2. Admin Login")

    @staticmethod
    def user_menu(courier_service):
        print("Courier Management System Customer Menu")
        print("1. Add User")
        print("2. View User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Place a new Courier Order")
        print("6. Get Order Status")
        print("7. Cancel a Courier Order")

        option = input("Enter the Operation number: ")
        if option == '1':
            user = MainModule.create_user()
            if courier_service.add_user(user):
                print("User added successfully.")
            else:
                print("Failed to add user.")

        elif option == '2':
            MainModule.view_user(courier_service)

        elif option == '3':
            MainModule.update_user(courier_service)

        elif option == '4':
            user_id = input("Enter user id to delete: ")
            if courier_service.delete_user(user_id):
                print("User deleted successfully.")
            else:
                print("Failed to delete user.")

        elif option == '5':
            user_id = input("Insert your user id: ")
            sender_name = input("Insert Sender name: ")
            sender_address = input("Insert Sender address: ")
            receiver_name = input("Insert Receiver name: ")
            receiver_address = input("Insert receiver address: ")
            weight = input("Insert weight of the courier: ")
            status = input("Insert courier status: ")
            tracking_number = input("Insert tracking number: ")
            delivery_date = input("Insert delivery date: ")

            courier = Courier(user_id, sender_name, sender_address, receiver_name, receiver_address, weight, status,
                              tracking_number, delivery_date, [])
            if courier_service.insert_order(courier):
                print("Order Placed successfully.")
            else:
                print("Failed to Place Order")

        elif option == '6':
            tracking_number = input("Insert tracking id of courier: ")
            get_status = courier_service.get_order_status(tracking_number)
            print(get_status)

        elif option == '7':
            tracking_number = input("Insert tracking id to cancel the order: ")
            cancel_order = courier_service.cancel_order(tracking_number)

    @staticmethod
    def create_user():
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        contact_number = input("Enter Contact Number: ")
        address = input("Enter Address: ")
        return User(None, name, email, password, contact_number, address)

    @staticmethod
    def view_user(courier_service):
        user_id = input("Enter user id to view: ")
        user = courier_service.get_user(user_id)
        if user:
            print("User Details:")
            print("User ID:", user.get_user_id())
            print("Name:", user.get_name())
            print("Email:", user.get_email())
            print("Contact Number:", user.get_contact_number())
            print("Address:", user.get_address())
        else:
            print("User not found.")

    @staticmethod
    def update_user(courier_service):
        user_id = input("Enter user id to update: ")
        user = courier_service.get_user(user_id)
        if user:
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            contact_number = input("Enter Contact Number: ")
            address = input("Enter Address: ")
            updated_user = User(user_id, name, email, password, contact_number, address)
            if courier_service.update_user(updated_user):
                print("User updated successfully.")
            else:
                print("Failed to update user.")
        else:
            print("User not found.")

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
            employee = Employee(employee_name, email, mobile_number, role, salary, [])
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
