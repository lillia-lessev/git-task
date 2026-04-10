"""
----------------------------------------------

Lillia Lessev
    
The String and Numerical Data Types
----------------------------------------------

"""

# Getting a string from the user
str_manip = input("Please enter a sentence: ")

#Calculating the length of the string
str_manip_length = len(str_manip)

print(f"The length of the string is: {str_manip_length}")


last_letter = str_manip[-1] #getting the last letter of the string
rep_str_manip = str_manip.replace(last_letter, "@") #replacing the last letter with @
print(f"The last letter of the original string was {last_letter}.\nThe new string is: {rep_str_manip}")

str_manip_piece = str_manip[-3:] #getting the last three letters of the string
str_manip_piece = str_manip_piece[::-1] #reversing the last three letters of the string
print(str_manip_piece)

first_three = str_manip[:3] #getting the first three letters of the string
last_two = str_manip[-2:] #getting the last two letters of the string
new_str_manip = first_three + last_two #concatenating the first three and last two letters of the string
print(new_str_manip)


