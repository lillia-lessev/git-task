"""
----------------------------------------------

Lillia Lessev

Iteration and loops

----------------------------------------------

"""

num = 1
my_condition = True
num_list = []

print("\n-----------------------------------\n")

while (num != -1):
    condition = True
    num = int(input("Please input an integer: "))
    if (num != 0):
        num_list.extend([num])
        list_length = len(num_list)
    elif (num == 0):
        print("This is not a valid response.")
    
else:
    if (num == -1):
        condition = False
    sum = 0
    for i in range(0, list_length):
        sum = num_list[i] + sum
    average = (sum / list_length)
    
    print("\nEnd of loop.\n")
    print(f"Amount of values entered: {list_length}")
    print(f"Sum of values: {sum}")
    print(f"Average: {average}")
    
print("\n-----------------------------------\n")

    