# Task 2: Loops and Iteration

# 1. Display all orders for a specific customer using a for loop
def display_customer_orders(orders, customer_id):
    print("Customer Orders:")
    for order in orders:
        if order["customer_id"] == customer_id:
            print("Order ID:", order["order_id"])
            print("Status:", order["status"])
            print("---------------")


# Test Task 2.1
orders = [
    {"order_id": 1, "customer_id": 101, "status": "Processing"},
    {"order_id": 2, "customer_id": 102, "status": "Delivered"},
    {"order_id": 3, "customer_id": 101, "status": "Cancelled"},
    {"order_id": 4, "customer_id": 103, "status": "Processing"}
]
customer_id_input = int(input("Enter the customer ID to display orders: "))
display_customer_orders(orders, customer_id_input)


# 2. Track real-time location of a courier using a while loop
def track_courier(courier_id, destination):
    print("Tracking Courier...")
    current_location = "Warehouse"
    while current_location != destination:
        print("Current Location:", current_location)
        current_location = input("Enter courier's current location: ")
    print("Courier reached its destination:", destination)


# Test Task 2.2
courier_id_input = int(input("Enter the courier ID: "))
destination_input = input("Enter the destination: ")
track_courier(courier_id_input, destination_input)
