"""
----------------------------------------------

Lillia Lessev
    
The String and Numerical Data Types
----------------------------------------------

"""

import math


print('''\n---------------------------------------\n
      Enter the lengths of the three sides of a triangle and press enter. Please only enter numbers and no measurements.\n''')

side1 = float(input('Side 1: '))
side2 = float(input('Side 2: '))
side3 = float(input('Side 3: '))

perimeter = side1 + side2 + side3
semi_perimeter = perimeter / 2

area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))

print(f'''\nThe total perimeter of the triangle is: {perimeter}
      \nThe perimeter divided by 2 is: {semi_perimeter}
      \nArea = The square root of ({semi_perimeter} x ({semi_perimeter}-{side1}) x ({semi_perimeter}-{side2}) x ({semi_perimeter}-{side3}))
      \nArea = {area}''')
print("\n---------------------------------------\n")
