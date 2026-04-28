"""
----------------------------------------------

Lillia Lessev

Programming With User-Defined Functions

----------------------------------------------

"""

print("\n--------------------------------------------------------\n")

# GETTING INPUT FROM USER
print("Please select your city destination:\n1 - New York (1000)\n2 - Paris (4000)\n3 - Venice (3000)")
city_flight = int(input("Enter the city number from the list: "))
num_nights = int(input("Number of nights of stay: "))
rental_days = int(input("Number of days renting car: "))

# HOTEL COST FUNCTION
def hotel_cost(num_nights):
    per_night = 500
    hotel_price = per_night * num_nights
    return hotel_price

# PLANE COST FUNCTION
def plane_cost(city_flight):
    if city_flight == 1:
        plane_price = 1000
    elif city_flight == 2:
        plane_price = 40000
    elif city_flight == 3:
        plane_price = 3000
    else:
        print("No valid city entered to calculate flight cost.")
        plane_price = 0
    return plane_price

# DESTINATION CITY FUNCTION
def dest_city(city_flight):
    if city_flight == 1:
        city = "New York"
    elif city_flight == 2:
        city = "Paris"
    elif city_flight == 3:
        city = "Venice"
    else:
        print("No valid city was entered.")
        city = "None"
    return city

# CAR RENTAL COST FUNCTION
def car_rental(rental_days):
    per_day = 150
    car_rent = per_day * rental_days
    return car_rent

# TOTAL HOLIDAY COST FUNCTION
def holiday_cost(num_nights, city_flight, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

# DISPLAYING DETAILS OF HOLIDAY
print("\n--------------------------------------------------------\n")
print("HOLDAY DETAILS:\n\n")
print(f"City: {dest_city(city_flight)}")
print(f"Flight cost: {plane_cost(city_flight)}")
print(f"\nNumber of nights at hotel: {num_nights}")
print(f"Total cost of hotel: {hotel_cost(num_nights)}")
print(f"\nNumber of days renting car: {rental_days}")
print(f"Car rental cost: {car_rental(rental_days)}")
print(f"\n\nTOTAL HOLIDAY COST:\n{holiday_cost(num_nights, city_flight, rental_days)}")

print("\n--------------------------------------------------------\n")
