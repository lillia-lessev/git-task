"""
----------------------------------------------

Lillia Lessev
    
The String and Numerical Data Types
----------------------------------------------

"""

print(f"\nPlease enter 3 different integer numbers and click enter.\n")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))        
num3 = int(input("Third number: "))

sum_num = num1 + num2 + num3
num_diff = num1 - num2
num_prod = num3 * num1
new_result = sum_num / num3
print(f"{num1} + {num2} + {num3} = {sum_num}")
print(f"{num1} - {num2} = {num_diff}")
print(f"{num3} * {num1} = {num_prod}")
print(f"{sum_num} / {num3} = {new_result}")
