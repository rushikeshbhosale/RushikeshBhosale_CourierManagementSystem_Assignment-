#dao/CourierUserServiceCollectionImpl.py

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
