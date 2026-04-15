# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

''' 
Original code:

animal = Lion
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

print full_spec


'''


animal = "Lion" # added quation marks
animal_type = "cub"
number_of_teeth = 16

full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth.") # added brackets () and braces {} for correct f-string format. Fixed order of variables in sentence, spacing etc.

print(full_spec) # added brackets for print statement

