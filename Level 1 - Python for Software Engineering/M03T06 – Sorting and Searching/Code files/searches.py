"""
----------------------------------------------

Lillia Lessev

Abstract Data Types

----------------------------------------------

"""

print("\n--------------------------------------------------------\n")

def sequential_search(target, items):
    # Iterate over the list. If we find the target item, return its index. 
    for index in range(len(items)):
        if items[index] == target:
            return index
    
    # If the target item is not found, return None. 
    return None
    
# Example usage: 
items_list = [50, 10, 40, 20, 30] 
target_item = 30
result = sequential_search(target_item, items_list)

if result is not None:
    print(f"Item {target_item} found at index {result}.")
else:
    print(f"Item {target_item} not found in the list.")
    
    
    
def binary_search(target, items):
    low, high = 0, len(items) - 1
    
    # Keep iterating until the low and high cross 
    while high >= low:
        # Find midpoint 
        mid = (low + high) // 2
        
        # If item is found at midpoint, return its index 
        if items[mid] == target:
            return mid 
        
        # Else, if item at midpoint is less than target, search the second half of the list
        elif items[mid] < target:
            low = mid + 1
        
        # Else, search the first half 
        else:
            high = mid - 1
    
    # Returns None if item not found 
    return None

# Example usage: 
sorted_items = [10, 20, 30, 40, 50] 
target_item = 50
result = binary_search(target_item, sorted_items)
print(f"Found at index {result}") 

print("\n--------------------------------------------------------\n")
