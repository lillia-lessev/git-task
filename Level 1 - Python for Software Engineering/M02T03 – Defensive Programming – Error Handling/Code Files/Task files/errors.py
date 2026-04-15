# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

''' 
print "Welcome to the error program"
    print "\n"
'''
# Adding brackets around what should be printed
print("Welcome to the error program.")
print("\n")

'''
    # Variables declaring the user's age, casting the str to an int, and printing the result
    age_Str == "24 years old" 
    age = int(age_Str) 
    print("I'm" + age + "years old.")

    # Variables declaring additional years and printing the total years of age
    years_from_now = "3"
    total_years = age + years_from_now 
    
    print "The total number of years:" + "answer_years"

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = total * 12
print "In 3 years and 6 months, I'll be " + total_months + " months old"


'''
# FIXED INDENTATION


# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24" # fixed variable name to be proper snake case and changed 'equal to' to 'assign'. Removed "years old"
age = int(age_str) 
print(f"I'm {age} years old.") # fixed spacing in string, made it an f-string for easier formatting

# Variables declaring additional years and printing the total years of age
years_from_now = 3 # making it an integer, not a string
total_years = age + years_from_now

print(f"{age} + {years_from_now} = {total_years}") # fixed brackets for print statement and spacing; fixed formatting by making it an f-string and using {}; fixed variabel name. Also fixed output message so that it's better understood.

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = (total_years * 12) + 6 #changing total to total_years, and adding 6 months
print(f"In {years_from_now} years and 6 months, I'll be {total_months} months old") # adding brackets for print statement, made it an f-string for easier formatting

#HINT, 330 months is the correct answer

