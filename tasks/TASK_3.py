"""
Task 3: Arrays and Data Structures
"""

# 1. Create an array to store the tracking history of a parcel, where each entry represents a location update.
class Parcel:
    def __init__(self):
        self.tracking_history = []

    def update_location(self, location):
        self.tracking_history.append(location)


# Example usage:
parcel = Parcel()
parcel.update_location("Warehouse")
parcel.update_location("In transit")
parcel.update_location("Arrived at destination")

print("Parcel Tracking History:")
for index, location in enumerate(parcel.tracking_history, start=1):
    print(f"{index}. {location}")


# 2. Implement a method to find the nearest available courier for a new order using an array of couriers.
class Courier:
    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location
        self.available = True


def find_nearest_courier(couriers, delivery_location):
    nearest_courier = None
    min_distance = float('inf')

    for courier in couriers:
        distance = abs(ord(courier.current_location) - ord(delivery_location))
        if courier.available and distance < min_distance:
            min_distance = distance
            nearest_courier = courier

    return nearest_courier


# Example usage:
couriers = [
    Courier("Courier A", "Warehouse A"),
    Courier("Courier B", "Warehouse B"),
    Courier("Courier C", "Warehouse C")
]

nearest_courier = find_nearest_courier(couriers, "Customer's Address")
if nearest_courier:
    print(f"Nearest available courier: {nearest_courier.name}")
else:
    print("No available couriers found.")
