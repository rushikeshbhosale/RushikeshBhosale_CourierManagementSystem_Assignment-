# Task 5: Object Oriented Programming
# Scope: Entity classes/Models/POJO, Abstraction/Encapsulation

# 1. User Class
class User:
    def __init__(self, userID, userName, email, password, contactNumber, address):
        self.__userID = userID
        self.__userName = userName
        self.__email = email
        self.__password = password
        self.__contactNumber = contactNumber
        self.__address = address

    # Getters and Setters
    def getUserID(self):
        return self.__userID

    def setUserID(self, userID):
        self.__userID = userID

    def getUserName(self):
        return self.__userName

    def setUserName(self, userName):
        self.__userName = userName

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def getContactNumber(self):
        return self.__contactNumber

    def setContactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    # toString method
    def __str__(self):
        return f"User(userID={self.__userID}, userName={self.__userName}, email={self.__email}, password={self.__password}, contactNumber={self.__contactNumber}, address={self.__address})"


# 2. Courier Class
class Courier:
    def __init__(self, courierID, senderName, senderAddress, receiverName, receiverAddress, weight, status,
                 trackingNumber, deliveryDate, userID):
        self.__courierID = courierID
        self.__senderName = senderName
        self.__senderAddress = senderAddress
        self.__receiverName = receiverName
        self.__receiverAddress = receiverAddress
        self.__weight = weight
        self.__status = status
        self.__trackingNumber = trackingNumber
        self.__deliveryDate = deliveryDate
        self.__userID = userID

    # Getters and Setters
    def getCourierID(self):
        return self.__courierID

    def setCourierID(self, courierID):
        self.__courierID = courierID

    def getSenderName(self):
        return self.__senderName

    def setSenderName(self, senderName):
        self.__senderName = senderName

    def getSenderAddress(self):
        return self.__senderAddress

    def setSenderAddress(self, senderAddress):
        self.__senderAddress = senderAddress

    def getReceiverName(self):
        return self.__receiverName

    def setReceiverName(self, receiverName):
        self.__receiverName = receiverName

    def getReceiverAddress(self):
        return self.__receiverAddress

    def setReceiverAddress(self, receiverAddress):
        self.__receiverAddress = receiverAddress

    def getWeight(self):
        return self.__weight

    def setWeight(self, weight):
        self.__weight = weight

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status

    def getTrackingNumber(self):
        return self.__trackingNumber

    def setTrackingNumber(self, trackingNumber):
        self.__trackingNumber = trackingNumber

    def getDeliveryDate(self):
        return self.__deliveryDate

    def setDeliveryDate(self, deliveryDate):
        self.__deliveryDate = deliveryDate

    def getUserID(self):
        return self.__userID

    def setUserID(self, userID):
        self.__userID = userID

    # toString method
    def __str__(self):
        return f"Courier(courierID={self.__courierID}, senderName={self.__senderName}, senderAddress={self.__senderAddress}, receiverName={self.__receiverName}, receiverAddress={self.__receiverAddress}, weight={self.__weight}, status={self.__status}, trackingNumber={self.__trackingNumber}, deliveryDate={self.__deliveryDate}, userID={self.__userID})"


# 3. Employee Class
class Employee:
    def __init__(self, employeeID, employeeName, email, contactNumber, role, salary):
        self.__employeeID = employeeID
        self.__employeeName = employeeName
        self.__email = email
        self.__contactNumber = contactNumber
        self.__role = role
        self.__salary = salary

    # Getters and Setters
    def getEmployeeID(self):
        return self.__employeeID

    def setEmployeeID(self, employeeID):
        self.__employeeID = employeeID

    def getEmployeeName(self):
        return self.__employeeName

    def setEmployeeName(self, employeeName):
        self.__employeeName = employeeName

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getContactNumber(self):
        return self.__contactNumber

    def setContactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def getRole(self):
        return self.__role

    def setRole(self, role):
        self.__role = role

    def getSalary(self):
        return self.__salary

    def setSalary(self, salary):
        self.__salary = salary

    # toString method
    def __str__(self):
        return f"Employee(employeeID={self.__employeeID}, employeeName={self.__employeeName}, email={self.__email}, contactNumber={self.__contactNumber}, role={self.__role}, salary={self.__salary})"


# 4. Location Class
class Location:
    def __init__(self, locationID, locationName, address):
        self.__locationID = locationID
        self.__locationName = locationName
        self.__address = address

    # Getters and Setters
    def getLocationID(self):
        return self.__locationID

    def setLocationID(self, locationID):
        self.__locationID = locationID

    def getLocationName(self):
        return self.__locationName

    def setLocationName(self, locationName):
        self.__locationName = locationName

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    # toString method
    def __str__(self):
        return f"Location(locationID={self.__locationID}, locationName={self.__locationName}, address={self.__address})"


# 5. CourierCompany Class
class CourierCompany:
    def __init__(self, companyName, courierDetails, employeeDetails, locationDetails):
        self.__companyName = companyName
        self.__courierDetails = courierDetails  # collection of Courier Objects
        self.__employeeDetails = employeeDetails  # collection of Employee Objects
        self.__locationDetails = locationDetails  # collection of Location Objects

    # Getters and Setters
    def getCompanyName(self):
        return self.__companyName

    def setCompanyName(self, companyName):
        self.__companyName = companyName

    def getCourierDetails(self):
        return self.__courierDetails

    def setCourierDetails(self, courierDetails):
        self.__courierDetails = courierDetails

    def getEmployeeDetails(self):
        return self.__employeeDetails

    def setEmployeeDetails(self, employeeDetails):
        self.__employeeDetails = employeeDetails

    def getLocationDetails(self):
        return self.__locationDetails

    def setLocationDetails(self, locationDetails):
        self.__locationDetails = locationDetails

    # toString method
    def __str__(self):
        return f"CourierCompany(companyName={self.__companyName}, courierDetails={self.__courierDetails}, employeeDetails={self.__employeeDetails}, locationDetails={self.__locationDetails})"


# 6. Payment Class
class Payment:
    def __init__(self, paymentID, courierID, amount, paymentDate):
        self.__paymentID = paymentID
        self.__courierID = courierID
        self.__amount = amount
        self.__paymentDate = paymentDate

    # Getters and Setters
    def getPaymentID(self):
        return self.__paymentID

    def setPaymentID(self, paymentID):
        self.__paymentID = paymentID

    def getCourierID(self):
        return self.__courierID

    def setCourierID(self, courierID):
        self.__courierID = courierID

    def getAmount(self):
        return self.__amount

    def setAmount(self, amount):
        self.__amount = amount

    def getPaymentDate(self):
        return self.__paymentDate

    def setPaymentDate(self, paymentDate):
        self.__paymentDate = paymentDate

    # toString method
    def __str__(self):
        return f"Payment(paymentID={self.__paymentID}, courierID={self.__courierID}, amount={self.__amount}, paymentDate={self.__paymentDate})"
