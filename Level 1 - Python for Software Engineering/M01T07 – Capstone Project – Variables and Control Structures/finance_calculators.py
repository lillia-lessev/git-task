"""
----------------------------------------------

Lillia Lessev

Capstone Project

----------------------------------------------

"""

"""
This is a python program showcasing everything learnt thus far in the course.
The purpose of this program is to calculate interest.
The program will calculate either:
the interest earned on a user's investment
or
the amount that should be repaid on a loan each month.

The formulas for both simple and compound interest are shown below for reference.
The formula for bond calculation is also shown below.


Simple Interest Formula:
A = P(1 + i(t))

Compound Interest:
A = P(1 + (i/n))^nt

A = total accured amount
P = principal amount
i = interest rate (percentage) PER time period
t = time period
n = number of times interst is compounded per time period

Formulas from: CalculatorSoup (2023).
See full reference list at the end of the project.

Bond repayment formula (FROM TASK PDF INSTRUCTIONS):

repayment = (i * P) / (1 - ((1 + i))^(-n))
i = interest rate PER MONTH (percentage)
n = number of months
P = Principle amount (present value of house)

"""

import math

print("\n--------------------------------------------\n")

# Declaring variables

# INVESTMENT
interest = ""
principal_amount = 0.0
accumulated_amount = 0.0
interest_rate = 0.0
rate_option = 0
time_period = 0.0
time_option = 0
years = 0.0
months = 0.0
compounded = 0
compounded_option = 0

# BOND
repayment = 0.0
present_value = 0.0
bond_interest_rate = 0.0
bond_months = 0.0


# Displaying instructional message to user and getting input for selcted option
print('''Investment -   to calculate the amount of interest you'll earn on your investment.\n
      Bond -   to calculate the amount you'll have to pay on a home loan.\n''')
option = input('''Enter either "investment" or "bond" from the menu above to proceed.\nPlease type the word exactly as shown without any extra spaces.\n
               Option: ''')
option = option.lower() # Converting input to lowercase incase user types in uppercase

# I learnt how to write while statements from w3schools (2024). See full reference list at the end of the program.
# Displaying error message if user input is incorrect / invalid 
while (option != "investment") and (option != "bond"):
    print('''\nInvalid Option. Please type your selected option exactly like the provided examples.\n
          Please type either "investment" or "bond" and try again.\n''')
    option = input("Option: ")
    option = option.lower() # Converting input to lowercase incase user types in uppercase
    print("------------------------------------------------\n")

else:
    #-----------INVESTMENT------------------------
    if (option == "investment"):
        print("\n------------------------------------------------\n")
        print("INVESTMENT\n")
        print("\nPlease enter the amount of money you are depositing and press ENTER. \nType the number ONLY.")
        principal_amount = float(input("Initial Amount Deposited: "))
        print("------------------------------------------------\n")

        
        """  
         # Determining if interest rate is per month or per year
        print('''Is your interest rate per YEAR or per MONTH?\n
              Please type only either "1" or "2" for your selected option.
              \n1 - Interest rate per YEAR
              \n2 - Interest rate per MONTH\n''')
        rate_option = int(input("Option: "))
        
        #Interest rate per year
        if (rate_option == 1): 
            print('''\nPlease enter your interest rate per year below.\n
                  Please ONLY type the NUMBER for your interest rate percentage.\n
                  Do NOT type the percentage symbol''')
            interest_rate = float(input("Interest Rate (%): "))
            interest_rate = interest_rate / 100 # Converting rate to percentage 
            interest_rate = (interest_rate * 12) # converting it to interest per month
        
        # Interest rate per month
        elif (rate_option == 2):
            print('''\nPlease enter your interest rate per month below.\n
                  Please ONLY type the NUMBER for your interest rate percentage.\n
                  Do NOT type the percentage symbol''')
            interest_rate = float(input("Interest Rate (%): "))
            interest_rate = interest_rate / 100 # Converting rate to percentage 
        
        """
        
        
        
        
        print('''\nPlease enter your interest rate PER YEAR below.\n*Please note that this calculator only works with ANNUAL INTEREST RATES and does not have the option to calculate monthly interest rates.*\n
              Please ONLY type the NUMBER for your interest rate percentage.\n
              Do NOT type the percentage symbol.''')
        interest_rate = float(input("\nInterest Rate Per Year (%): "))
        interest_rate = interest_rate / 100 # Converting rate to percentage 
        #interest_rate = (interest_rate * 12) # converting it to interest per month
        print("------------------------------------------------\n")
      

        # Determining how user wants to input time period for investment
        print('''\nPlease select the way you want to input the time period for which your investment will be.\n\n
              1 - Total number of MONTHS\n
              2 - Total number of YEARS\n
              3 - Total number of YEARS and MONTHS e.g. x Years, x Months\n\n
              Please type ONLY the number "1", "2", or "3" and press ENTER.''')
        time_option = int(input("Option: "))
        print("------------------------------------------------\n")
        
        # MONTHS
        if (time_option == 1):
            print('''\nPlease enter the total number of MONTHS for your investment and press ENTER. Type the number only.\nIf it is not a WHOLE number of months, then please type your total number of months as a DECIMAL number.\n
                  e.g. 1 1/2 Months should be typed as "1.5" etc.\n''')
            time_period = float(input("Total Number of MONTHS: "))
            time_period = (time_period / 12) # converting to years
            print("------------------------------------------------\n")

            
        # YEARS
        elif (time_option == 2):
            print('''\nPlease enter the total number of YEARS for your investment and press ENTER. Type the number only.\nIf it is not a WHOLE number of years, then please type your total number of years as a DECIMAL number.\n
                  e.g. 1 1/2 Years should be typed as "1.5" etc.\n''')
            time_period = float(input("Total Number of YEARS: "))
            print("------------------------------------------------\n")

            
        # YEARS AND MONTHS   
        elif (time_option == 3):
            print('''\nPlease enter the total number of YEARS for your investment FIRST and press ENTER. Then enter the total number of MONTHS afterwards.\n
                  Type the number only.\n
                  Please enter a WHOLE number for the number of YEARS.\n''')
            time_period_years = float(input("Total Number of YEARS: "))
            
            time_period_years = math.trunc(time_period) # Truncating the number of years to a whole number in case user types in a decimal
            print('''\nNow please enter the total number of MONTHS for your investment and press ENTER. Type the number only.\nIf it is not a WHOLE number of months, then please type your total number of months as a DECIMAL number.\n
                  e.g. 1 1/2 Months should be typed as "1.5" etc.\n''')
            time_period_months = float(input("Total number of MONTHS: "))
            time_period = (time_period_years * 12) + time_period_months # Getting TOTAL number of MONTHS
            time_period = (time_period / 12) # Converting to years
            print("------------------------------------------------\n")


        # Invalid response error message.   
        else:
            print('''That was not a valid response. Please make sure to read the prompted instructions carefully and follow them exactly.\n
                  Restart the program and try again.\n''')
    
    
        # Selecting type of interest
        print('''Please select the type of interest you want to calculate.\n
            1 - Simple Interest\n
            2 - Compound Interest\n
            Please type ONLY the number "1" or "2" for your selected option and press ENTER.\n''')
        interest = int(input("Option: "))
        print("------------------------------------------------\n")

        
        # SIMPLE INTEREST
        if (interest == 1):
            print("\n--------------------------------------------\n")
            print("SIMPLE INTEREST\n\n")
            print(f'''A=P(1 + i(t))\n\n''')
            print(f'''A = Total Accumulated Amount\n
                  P = {principal_amount}\n
                  i = {interest_rate}\n
                  t = {time_period}''')
            accumulated_amount = float((principal_amount * (1 + (interest_rate * time_period))))
            print(f'''\nThe total amount of money earned at the end of your investment is valued at:\n
                  {accumulated_amount}''')
            accumulated_amount = round(accumulated_amount, 2) # rounding total amount to 2 decimal places
            print(f'''\nThe rounded amount is:\n
                  {accumulated_amount}''')
            print("\n--------------------------------------------\n")
        
        # COMPOUND INTEREST       
        elif (interest == 2):
            print("\n--------------------------------------------\n")
            print("COMPOUND INTEREST\n\n")
            print(f'''A = P(1 + (i/n))^tn\n\n''')
            print(f'''A = Total Accumulated Amount\n
                  P = {principal_amount}\n
                  i = {interest_rate}\n
                  t = {time_period}\n 
                  n = {compounded}''')
            
            # Choosing if interest is compounded monthly or annually
            print('''\n\nIs the interest compounded ANNUALLY or MONTHLY?\n
                  1 - ANNUALLY\n
                  2 - MONTHLY\n
                  Please only type either the number "1" or "2".''')
            compounded_option = int(input("Option: "))
            
            # COMPOUNDED ANNUALLY
            if (compounded_option == 1):
                compounded = 1
                
            # COMPOUNDED MONTHLY
            elif (compounded_option == 2):
                compounded = 12
                
            # ERROR
            else:
                print('''That was not a valid response. Please make sure to read the prompted instructions carefully and follow them exactly.\n
                      Restart the program and try again.\n''')
            
            accumulated_amount = float((principal_amount * (math.pow((1 + (interest_rate / compounded)), (time_period * compounded)))))
            print(f'''The total amount of money earned at the end of your investment is valued at:\n
                  {accumulated_amount}''')
            accumulated_amount = round(accumulated_amount, 2) # rounding total amount to 2 decimal places
            print(f'''\nThe rounded amount is:\n
                  {accumulated_amount}''')
            print("\n--------------------------------------------\n")
  
            
        else:
            print('''That was not a valid response. Please make sure to read the prompted instructions carefully and follow them exactly.\n
                  Restart the program and try again.\n''')
    
    
    
    
    
        print("\n\n Thank you for using my finance calculator!")
        print("\n--------------------------------------------\n")
            
    
    
    
    #-----------BOND------------------------
    elif (option == "bond"):
        print("\n------------------------------------------------\n")
        print("BOND\n")
        
        # PRESENT VALUE
        print("\nPlease enter the present value of the house and press ENTER. \nType the number ONLY.")
        present_value = float(input("Present Value: "))
        print("------------------------------------------------\n")
        
         # INTEREST RATE
        print('''\nPlease enter the MONTHLY interest rate (interest rate PER MONTH) below.\n
              Please ONLY type the NUMBER for your interest rate percentage.\n
              Do NOT type the percentage symbol.''')
        bond_interest_rate = float(input("\nInterest Rate Per Month (%): "))
        bond_interest_rate = bond_interest_rate / 100 # Converting rate to percentage 
        print("------------------------------------------------\n")
        
        # NO. OF MONTHS
        print('''\nPlease enter the total number of MONTHS over which the bond will be repaid and press ENTER. Type the number only.\nIf it is NOT a WHOLE number of months, then please type your total number of months as a DECIMAL number.\n
              e.g. 1 1/2 Months should be typed as "1.5" etc.\n''')
        bond_months = float(input("Total number of MONTHS: "))
        print("------------------------------------------------\n")
        
        # CALCULATING AND DISPLAYING RESULTS
        print("\nBOND REPAYMENT CALCULATION\n\n")
        
        print(f'''Monthly repayment = (i * P) / (1 - ((1 + i))^(-n))\n\n
              i = {bond_interest_rate}\n 
              n = {bond_months}\n 
              P = {present_value} (present value of house)\n''')
        
        repayment = (bond_interest_rate * present_value) / (1 - (((1 + bond_interest_rate))**(0-bond_months)))

        print(f'''The total amount of money that needs to be repaid each month is valued at:\n
                  {repayment}''')
        repayment = round(repayment, 2) # rounding total amount to 2 decimal places
        print(f'''\nThe rounded amount is:\n
                  {repayment}''')
        print("\n--------------------------------------------\n")



        # EXITING MESSAGE
        print("\n\n Thank you for using my finance calculator!\n")
        print("\n--------------------------------------------\n")


    else:
        print('''That was not a valid response. Please make sure to read the prompted instructions carefully and follow them exactly.\n
                  Restart the program and try again.\n''')


""" 
-----------------------------------------
REFERENCES (APA 7th Edition Referencing Style)
-----------------------------------------

CalculatorSoup. (2023). Interest and APR Calculators. CalculatorSoup. https://www.calculatorsoup.com/calculators/financial/index-interest-apr-calculators.php 
w3schools. (2024). Python While Loops. Www.w3schools.com. https://www.w3schools.com/python/python_while_loops.asp 

"""