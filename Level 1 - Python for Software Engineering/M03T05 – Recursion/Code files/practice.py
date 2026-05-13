"""
----------------------------------------------

Lillia Lessev

Recursion

----------------------------------------------

"""

print("\n--------------------------------------------------------\n")

def factorial(n):
    # Base case: if n is 0, return 1 because 0! is defined as 1 
    if n == 0:
        return 1
    else:
    # Recursive case: calculate n! by multiplying n with the factorial of (n - 1)
        return n * factorial(n - 1)

print(f"The factorial of 4 is {factorial(4)}")

print("\n--------------------------------------------------------\n")