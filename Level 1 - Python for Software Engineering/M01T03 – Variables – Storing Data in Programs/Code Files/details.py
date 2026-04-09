"""
----------------------------------------------

Lillia Lessev
    
Variables - Storing Data in Programs

----------------------------------------------

"""
# Getting data from user    


user_name = str(input("Please enter your name: "))
user_age = input("Please enter your age (as a NUMBER, not a word): ")
user_age = int(user_age)
house_number = int(input("Please enter your house NUMBER: "))
street_name = str(input("Please enter your street name: "))


# Displaying the data back to the user
print(f"This is {user_name}. {user_name} is {user_age} years old and lives at {house_number} {street_name}.")

