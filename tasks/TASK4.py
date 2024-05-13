
"""
Task 4: Strings, 2D Arrays, User Defined Functions, Hashmap
"""

# 1. Parcel Tracking
class ParcelTracking:
    def __init__(self):
        self.tracking_data = [
            ["123456", "Parcel in transit"],
            ["789012", "Parcel out for delivery"],
            ["345678", "Parcel delivered"]
        ]

    def track_parcel(self, tracking_number):
        for data in self.tracking_data:
            if data[0] == tracking_number:
                return data[1]
        return "Invalid tracking number"


# Example usage:
parcel_tracking = ParcelTracking()
tracking_number = input("Enter parcel tracking number: ")
status = parcel_tracking.track_parcel(tracking_number)
print(status)


# 2. Customer Data Validation
def validate_customer_info(data, detail):
    if detail == "name":
        return data.isalpha() and data.istitle()
    elif detail == "address":
        return data.isalnum()
    elif detail == "phone number":
        return len(data) == 12 and data[3] == data[7] == '-' and data[:3].isdigit() and data[4:7].isdigit() and data[8:].isdigit()


# Example usage:
name = input("Enter customer name: ")
print("Name validation:", validate_customer_info(name, "name"))

address = input("Enter customer address: ")
print("Address validation:", validate_customer_info(address, "address"))

phone_number = input("Enter customer phone number (###-###-####): ")
print("Phone number validation:", validate_customer_info(phone_number, "phone number"))


# 3. Address Formatting
def format_address(street, city, state, zip_code):
    return f"{street.title()}, {city.title()}, {state.upper()} {zip_code}"


# Example usage:
street = input("Enter street: ")
city = input("Enter city: ")
state = input("Enter state: ")
zip_code = input("Enter zip code: ")
print("Formatted address:", format_address(street, city, state, zip_code))


# 4. Order Confirmation Email
def generate_order_confirmation_email(customer_name, order_number, delivery_address, expected_delivery_date):
    return f"Dear {customer_name},\n\nYour order ({order_number}) has been confirmed.\nDelivery Address: {delivery_address}\nExpected Delivery Date: {expected_delivery_date}\n\nThank you for choosing our services!\n\nRegards,\nCourier Management Team"


# Example usage:
customer_name = input("Enter customer name: ")
order_number = input("Enter order number: ")
delivery_address = input("Enter delivery address: ")
expected_delivery_date = input("Enter expected delivery date: ")
print("Order confirmation email:")
print(generate_order_confirmation_email(customer_name, order_number, delivery_address, expected_delivery_date))


# 5. Calculate Shipping Costs
def calculate_shipping_cost(source_address, destination_address, weight):
    # Simulated calculation based on distance and weight
    distance = 10  # Placeholder for distance calculation
    shipping_cost = distance * weight  # Placeholder for shipping cost calculation
    return shipping_cost

# Example usage:
source_address = "123 Main St, City A, State A, 12345"
destination_address = "456 Elm St, City B, State B, 67890"
weight = 5  # in kg
cost = calculate_shipping_cost(source_address, destination_address, weight)
print("Shipping cost:", cost)


# 6. Password Generator
import random
import string

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))


# Example usage:
print("Generated password:", generate_password())


# 7. Find Similar Addresses
def find_similar_addresses(address, address_list):
    similar_addresses = []
    for addr in address_list:
        if address.lower() in addr.lower() or addr.lower() in address.lower():
            similar_addresses.append(addr)
    return similar_addresses

# Example usage:
address_list = ["123 Main St", "456 Elm St", "789 Oak St", "Main St 123"]
address = "Main St"
similar_addresses = find_similar_addresses(address, address_list)
print("Similar addresses:", similar_addresses)
