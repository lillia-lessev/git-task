"""
----------------------------------------------

Lillia Lessev

Data Structures - Lists and Dictionaries


----------------------------------------------

"""

print("\n--------------------------------------------------------\n")


my_str = input("Please enter the correct name: ")
my_str = my_str.lower()
my_list = []

while (my_str != "john"):
    my_str = input("Please enter the correct name: ")
    my_str = my_str.lower()
    my_list.append([my_str])
else:
    if (my_str == "john"):
        print(f"The correct name 'John' was entered.")
        print(f"Incorrect names: {my_list}")
        
print("\n--------------------------------------------------------\n")