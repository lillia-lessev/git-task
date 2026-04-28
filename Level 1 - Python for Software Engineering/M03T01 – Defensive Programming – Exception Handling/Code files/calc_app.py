"""
----------------------------------------------

Lillia Lessev

Defensive programming - Exception Handling 

----------------------------------------------

"""

print("\n--------------------------------------------------------\n")

calc_state = True
prev_state = True
num1 = ""
num2 = ""
oper = ""
response = ""
calculation = ""

print("CALCULATOR:\n\n")
print("The calculator can perform simple operations that consist of two numbers and one operand. e.g.\n Value 1 (Operation) Value 2 = ANSWER")


# RUNNING CALCULATOR
def run_calc(response):
    while (response != "y") or (response != "n"):
        response = input("\nDo you want to try the calculator? (Y/N): ")
        response = response.lower()
        if response == "y":
            calc_state = True
            print("Great! Let's begin.\n\n")
            break
        elif response == "n":
            calc_state = False
            break  
        elif (response != "y") and (response != "n"):
            print("Not a valid response.")  
            calc_state = False
    return calc_state


# DECIDING TO SHOW PREVIOUS OPERATIONS
def show_prev(response):
    while (response != "y") or (response != "n"):
        response = input("\nDo you want to see the previous calculations? (Y/N): ")
        response = response.lower()
        if response == "y":
            prev_state = True
            print("Great! Here are the previous calculations.\n\n")
            break
        elif response == "n":
            prev_state = False
            print("\nBYE!")
            break  
        elif (response != "y") and (response != "n"):
            print("Not a valid response.")  
            prev_state = False
    return prev_state



calc_state = run_calc(response)        
while calc_state == True:  
    
    # GETTING NUM 1
    try:
        num1 = float((input("\nPlease enter the first value: ")))
    except Exception as error:
        if not isinstance(num1, float):
            print("\nError. Not a valid number. Please try again.")
            break    
            
    # GETTING OPERATOR
    print("Please enter one operand. e.g.\n+\n-\n/\n*")
    oper = input("Please enter the operation: ")
    if (oper != "+") and (oper != "-") and (oper != "/") and (oper != "*"):
        print("\nError. Not a valid operation. Please try again.")  
        break 
    
    # GETTING NUM 2
    try:
        num2 = float(input("Please enter the second value: "))    
    except Exception as error:
        if not isinstance(num2, float) :
            print("\nError. Not a valid number. Please try again.")
            break 
    
    # PERFORMING CALCULATION    
    if (oper == "+"):
        answer = num1 + num2
        calculation = f"{num1} + {num2} = {answer}"
        print(calculation)
    elif (oper == "-"):
        answer = num1 - num2
        calculation = f"{num1} - {num2} = {answer}"
        print(calculation)
    elif (oper == "/"):
        try:
            answer = num1 / num2
            calculation = f"{num1} / {num2} = {answer}"
            print(calculation)
        except ZeroDivisionError:
            print("Error. Cannot divide a number by zero.")
    elif (oper == "*"):
        answer = num1 * num2
        calculation = f"{num1} * {num2} = {answer}"
        print(calculation)
    
    
    # WRITING TO FILE
    try:
        with open ("equations.txt", "a+", encoding="utf-8") as file:
            file.write(calculation + "\n")
        print("Calculation has been written to file.")
    except FileNotFoundError:
        print("File does not exist.")

    # RUNNING CALCULATOR
    calc_state = run_calc(response)



# DISPLAYING PREVIOUS OPERATION
prev_state = show_prev(response)   
if prev_state == True:
    contents = ""
    try:
        with open ("equations.txt", "r+", encoding="utf-8") as file:
            for line in file:
                contents = contents + line
        print(contents)
    except FileNotFoundError:
        print("File does not exist.")
    
print("\n--------------------------------------------------------\n")