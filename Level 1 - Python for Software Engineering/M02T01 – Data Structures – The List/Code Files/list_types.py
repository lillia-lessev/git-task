"""
----------------------------------------------

Lillia Lessev

Data Structures - The List

----------------------------------------------

"""

# LISTS
friends_names = []
friends_ages = []


# OTHER VARIABLES
name1 = "Tom Jones"
name2 = "Bob Smith"
name3 = "Sam Fisher"
num = 0
age_counter = 0


# ADDING NAMES TO LIST
friends_names.insert(0, name1)
friends_names.insert(1, name2)
friends_names.insert(2, name3)


# AMOUNT OF NAMES IN LIST
list_length = len(friends_names)
print("\n-------------------------------------------\n")


# DISPLAYING 1st and 3rd Friend
print("1st AND 3rd FRIEND:\n")
print(f"Friend 1: {name1}\nFriend 3: {name3}")
print(f"There are {len(friends_names)} friends in the list.")
print("\n-------------------------------------------\n")


# DISPLAYING ALL FRIENDS
print("ALL FRIENDS:\n")

while num < list_length:
    print(f"Friend {num + 1}: {friends_names[num]}")
    num += 1

print(f"There are {list_length} friends in the list.")
print("\n-------------------------------------------\n")


# GETTING AGES AND STORING THEM
print("DETERMINING AGES OF FRIENDS:\n")
while age_counter < list_length:
    print(f"Friend {age_counter + 1}: {friends_names[age_counter]}")
    age = int(input(f"Input the age of {friends_names[age_counter]}: "))
    friends_ages.insert(age_counter, age)
    age_counter += 1
print("\n-------------------------------------------\n")


# DISPLAYING AGES
print("AGES OF ALL FRIENDS:\n")
age_counter = 0
while age_counter < list_length:
    print(f"Friend {age_counter + 1} is {friends_names[age_counter]} and they are {friends_ages[age_counter]} years old.")
    age_counter += 1
print("\n-------------------------------------------\n")
