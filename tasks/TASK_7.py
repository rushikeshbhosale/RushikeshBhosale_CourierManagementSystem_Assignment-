# Task 7: Exception Handling
# (Scope: User Defined Exception/Checked /Unchecked Exception/Exception handling using try..catch finally,thow & throws keyword usage)

# Define custom exceptions

# 1. TrackingNumberNotFoundException
class TrackingNumberNotFoundException(Exception):
    """
    Exception raised when a tracking number is not found.
    """

    def __init__(self, message="Tracking number not found"):
        self.message = message
        super().__init__(self.message)


# 2. InvalidEmployeeIdException
class InvalidEmployeeIdException(Exception):
    """
    Exception raised when an invalid employee ID is encountered.
    """

    def __init__(self, message="Invalid employee ID"):
        self.message = message
        super().__init__(self.message)


# Define a sample class demonstrating exception handling
class Example:
    def __init__(self):
        # Sample data for tracking numbers and employee IDs
        self.tracking_numbers = ["123456789", "987654321"]
        self.employee_ids = [1001, 1002]

    def withdrawAmount(self, trackingNumber):
        # Check if tracking number exists
        if not self.checkTrackingNumber(trackingNumber):
            raise TrackingNumberNotFoundException()

    def transferAmount(self, employeeId):
        # Check if employee ID exists
        if not self.checkEmployeeId(employeeId):
            raise InvalidEmployeeIdException()

    # Sample methods to check tracking number and employee ID
    def checkTrackingNumber(self, trackingNumber):
        # Check if tracking number exists in the list
        return trackingNumber in self.tracking_numbers

    def checkEmployeeId(self, employeeId):
        # Check if employee ID exists in the list
        return employeeId in self.employee_ids


# Main method demonstrating exception handling
if __name__ == "__main__":
    example = Example()
    try:
        example.withdrawAmount("123456789")  # This will raise TrackingNumberNotFoundException
    except TrackingNumberNotFoundException as e:
        print("Error:", e.message)

    try:
        example.transferAmount(1001)  # This will raise InvalidEmployeeIdException
    except InvalidEmployeeIdException as e:
        print("Error:", e.message)
