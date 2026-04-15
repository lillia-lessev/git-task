"""
----------------------------------------------

Lillia Lessev

Iteration and loops

----------------------------------------------

"""

num = 0
stars = ""
string_length = 0

print("\n\n")

for i in range(1, 9):
    if (i < 6):
        stars = stars + "*"
        string_length = len(stars)
        print(stars)
    elif (i >=6):
        string_length = len(stars)
        empty_char = ""
        stars = stars[:(string_length - 1)]
        string_length = len(stars)
        print(stars)
    
    
print("\n\n")

    