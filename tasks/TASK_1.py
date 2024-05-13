# Task 1: Check order delivery status
def check_order_status(status):
    if status.lower() == "delivered":
        print("The order is delivered.")
    elif status.lower() == "processing":
        print("The order is still processing.")
    elif status.lower() == "cancelled":
        print("The order is cancelled.")
    else:
        print("Invalid order status.")


# Test Task 1
order_status = input("Enter the status of the order: ")
check_order_status(order_status)


# Task 2: Categorize parcels based on weight
def categorize_parcel(weight):
    if weight < 5:
        print("Light parcel")
    elif 5 <= weight < 15:
        print("Medium parcel")
    else:
        print("Heavy parcel")


# Test Task 2
parcel_weight = float(input("Enter the weight of the parcel: "))
categorize_parcel(parcel_weight)


# Task 3: User Authentication
def user_authentication(username, password):
    # Simulating database lookup
    users = {"admin": "admin@123", "user": "user@123"}

    if username in users:
        if users[username] == password:
            print("Authentication successful. Welcome,", username)
        else:
            print("Incorrect password.")
    else:
        print("User not found.")


# Test Task 3
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
user_authentication(username_input, password_input)


# Task 4: Courier Assignment Logic
def assign_courier(shipments):
    for shipment in shipments:
        if shipment["proximity"] < 10 and shipment["load_capacity"] < 100:
            print("Assigning courier to shipment:", shipment["shipment_id"])
        else:
            print("Unable to assign courier to shipment:", shipment["shipment_id"])


# Test Task 4
shipments = [
    {"shipment_id": 1, "proximity": 5, "load_capacity": 80},
    {"shipment_id": 2, "proximity": 15, "load_capacity": 120},
    {"shipment_id": 3, "proximity": 8, "load_capacity": 90}
]
assign_courier(shipments)
