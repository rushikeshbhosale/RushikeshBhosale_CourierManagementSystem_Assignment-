from abc import ABC, abstractmethod


# Task 6: Service Provider Interface /Abstract class
# Create 2 Interface /Abstract class ICourierUserService and ICourierAdminService interface

# ICourierUserService interface
class ICourierUserService(ABC):
    """
    ICourierUserService interface for customer-related functions.
    """

    # Task 6: Customer-related functions
    @abstractmethod
    def placeOrder(self, courierObj):
        """Place a new courier order.

        Args:
            courierObj (Courier): Courier object created using values entered by users.

        Returns:
            str: The unique tracking number for the courier order.
        """
        pass

    @abstractmethod
    def getOrderStatus(self, trackingNumber):
        """Get the status of a courier order.

        Args:
            trackingNumber (str): The tracking number of the courier order.

        Returns:
            str: The status of the courier order (e.g., yetToTransit, In Transit, Delivered).
        """
        pass

    @abstractmethod
    def cancelOrder(self, trackingNumber):
        """Cancel a courier order.

        Args:
            trackingNumber (str): The tracking number of the courier order to be canceled.

        Returns:
            bool: True if the order was successfully canceled, False otherwise.
        """
        pass

    @abstractmethod
    def getAssignedOrder(self, courierStaffId):
        """Get a list of orders assigned to a specific courier staff member.

        Args:
            courierStaffId (int): The ID of the courier staff member.

        Returns:
            list: A list of courier orders assigned to the staff member.
        """
        pass


# ICourierAdminService interface
class ICourierAdminService(ABC):
    """
    ICourierAdminService interface for admin functions.
    """

    # Task 6: Admin functions
    @abstractmethod
    def addCourierStaff(self, name, contactNumber):
        """Add a new courier staff member to the system.

        Args:
            name (str): The name of the courier staff member.
            contactNumber (str): The contact number of the courier staff member.

        Returns:
            int: The ID of the newly added courier staff member.
        """
        pass
