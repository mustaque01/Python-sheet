# Parent class Vehicle
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        # Default fare charge is seating_capacity * 100
        return self.seating_capacity * 100

# Child class Bus that inherits from Vehicle
class Bus(Vehicle):
    def __init__(self, seating_capacity):
        # Initialize the parent class with seating_capacity
        super().__init__(seating_capacity)

    def calculate_fare(self):
        # Get the original fare from the parent class
        total_fare = super().calculate_fare()
        
        # Add 10% maintenance charge on the total fare for the bus
        maintenance_charge = total_fare * 0.10
        
        # Final fare is the total fare plus the maintenance charge
        return total_fare + maintenance_charge

# Example Usage:
# Creating a Vehicle instance
vehicle = Vehicle(50)  # 50 seats
print("Vehicle Fare:", vehicle.calculate_fare())

# Creating a Bus instance
bus = Bus(50)  # 50 seats in the bus
print("Bus Fare:", bus.calculate_fare())
