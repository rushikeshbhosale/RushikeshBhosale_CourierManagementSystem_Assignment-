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
