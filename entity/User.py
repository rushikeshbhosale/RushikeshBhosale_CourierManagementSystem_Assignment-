#entity/User.py

class User:
    def __init__(self, UserID, Name, Email, Password, ContactNumber, Address):
        self.__UserID = UserID
        self.__Name = Name
        self.__Email = Email
        self.__Password = Password
        self.__ContactNumber = ContactNumber
        self.__Address = Address

    # Getter methods
    def get_user_id(self):
        return self.__UserID

    def get_name(self):
        return self.__Name

    def get_email(self):
        return self.__Email

    def get_password(self):
        return self.__Password

    def get_contact_number(self):
        return self.__ContactNumber

    def get_address(self):
        return self.__Address

    # Setter methods
    def set_user_id(self, UserID):
        self.__UserID = UserID

    def set_name(self, Name):
        self.__Name = Name

    def set_email(self, Email):
        self.__Email = Email

    def set_password(self, Password):
        self.__Password = Password

    def set_contact_number(self, ContactNumber):
        self.__ContactNumber = ContactNumber

    def set_address(self, Address):
        self.__Address = Address
