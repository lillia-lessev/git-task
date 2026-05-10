# Parent class for a car which we can extend to a subclass 
class Car:
    # Class variable for whether the engine is running or not 
    is_running = False
    
    # Constructor that allows us to set the make and model as instance variables
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    # Method to start the engine 
    def start_car(self):
        self.is_running = True
    
    # Method to turn off the engine 
    def turn_off_car(self):
        self.is_running = False
        
    # Method to print the make and model 
    def show_make_and_model(self):
        print(f"This vehicle is a {self.make} {self.model}")




# We are inheriting all of the attributes and methods from the Car class by passing it as an argument to the PickupTruck class 
class PickupTruck(Car):
    # This is an additional class variable that is specific to the PickupTruck class
    is_loaded = False
    
# Method to load the truck
def load(self):
    self.is_loaded = True
    
# Method to remove the load from the truck 
def unload(self):
    self.is_loaded = False




# Create a pickup truck object 
pickup_truck_1 = PickupTruck("Toyota", "Hilux")

# Call the load method that we created in the subclass 
# This changes the variable from False to True
pickup_truck_1.load()

# Call the start_car method inherited from the parent class 
pickup_truck_1.start_car()

# Print out to values so that we can see that both of the above methods worked
print(pickup_truck_1.is_running) 
print(pickup_truck_1.is_loaded)

# Call another method that was inherited from the parent class 
pickup_truck_1.show_make_and_model()