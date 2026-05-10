"""
----------------------------------------------

Lillia Lessev

OOP - Inheritance

----------------------------------------------

"""

class Adult:
    def __init__(self, name, age, eye_color, hair_color):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color

    def can_drive(self):
        print(f"{name} is old enough to drive.")        
    
class Child(Adult):
    def can_drive(self):
        print(f"{name} is too young to drive.")        

print("\n--------------------------------------------------------\n")

name = input("Enter name: ")
age = int(input("Enter age: "))
eye_color = input("Enter eye color: ")
hair_color = input("Enter hair color: ")

if age >= 18:
    person = Adult(name, age, eye_color, hair_color)
    person.can_drive()
elif (age < 18) and (age >= 0):
    person = Child(name, age, eye_color, hair_color)
    person.can_drive()
elif age < 0:
    print("Invalid age.")

print("\n--------------------------------------------------------\n")