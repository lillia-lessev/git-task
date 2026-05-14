"""
----------------------------------------------

Lillia Lessev

Abstract Data Types

----------------------------------------------

"""


""" 
For the given list, I have decided to use sequential searching since it is an unordered list.
"""

import math

print("\n--------------------------------------------------------\n")


# LINEAR / SEQUENTIAL SEARCH
def sequential_search(target, items):
    # Iterate over the list. If we find the target item, return its index. 
    for index in range(len(items)):
        if items[index] == target:
            return index
    
    # If the target item is not found, return None. 
    return None


# Linear / Sequential search for number 9   
num_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target_item = 9
index = sequential_search(target_item, num_list)

# Printing linear / Sequential Search
print(f"Original list:\n{num_list}")
if index is not None:
    print(f"The number {target_item} was found at index {index}.")
else:
    print(f"The number {target_item} was not found in the list.")


# INSERTION SORT
# Learnt about Insertion Sort from FelixTechTips (2020). Full reference at the end, in reference list.
def insertion_sort(num_list):
    
    for i in range(1, len(num_list)):
        j = i 
        while (num_list[j - 1 ] > num_list[j]) and (j > 0):
            # Swapping elements
            '''
            temp = num_list[j - 1]
            num_list[j - 1] = num_list[j]
            num_list[j] = temp
            '''
            num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]
            j -= 1
    
    return num_list

# Insertion Sorting List
ins_sorted_list = insertion_sort(num_list)
print("\nSorted list using insertion method:")
print(ins_sorted_list)

''' 
For this particular list in this task, I have decided to use the binary search to search for the number 9.
The binary search works with ordered lists and since I have already sorted the list in this program, I can then 
proceed and search the list using the binary search method.
In the real world, binary search would work with ordered sets of data e.g. a list of books sorted alphabetically by title, author etc. 
'''
# --- BINARY SEARCH ---
def binary_search(sorted_list, target):
    low = 0
    current_length = len(sorted_list)
    high = len(sorted_list) - 1
    mid = high // 2
    
    while high >= low:
        # mid = math.trunc(high / 2)
        #mid = high // 2 # The double // truncates the answer
        current = sorted_list[mid]
        if sorted_list[mid] == target:
            #print(f"The number {target} was found at index {mid}.")
            return mid
        elif sorted_list[mid] < target:
            low = mid
            mid = (low + high) // 2
            
        elif sorted_list[mid] > target:
            high = mid
            mid = high // 2
            
    

# Displaying index of number using binary search
new_index = binary_search(ins_sorted_list, target_item)
print("\nBinary search:")
print(f"The number {target_item} was found at index {new_index} in the sorted list.")

print("\n--------------------------------------------------------\n")


''' 
---- REFERENCES ----

FelixTechTips. (2020, June 12). Insertion Sort In Python Explained (With Example And Code). YouTube. https://youtu.be/R_wDA-PmGE4

'''
