"""
----------------------------------------------

Lillia Lessev

Abstract Data Types

----------------------------------------------

"""

print("\n--------------------------------------------------------\n")


def quick_sort(my_list, low, high):
    if low < high:
        # Partition the list and get the pivot index 
        mid = partition(my_list, low, high)
        
        # Recursively sort the left partition 
        my_list = quick_sort(my_list, low, mid - 1)
        
        # Recursively sort the right partition 
        my_list = quick_sort(my_list, mid + 1, high)
        
    return my_list

def partition(my_list, low, high):
    # The pivot point is the first item in the sublist 
    pivot = my_list[low]
    
    # Loop through the list. Move items up or down the list so that they are in the proper spot with regard to the pivot point
    while low < high:
        
        # Can we find a number smaller than the pivot point: 
        # Keep moving the high marker down the list until we find this or until high==low
        while low < high and my_list[high] >= pivot:
            high -= 1
            
        if low < high:
            # Found a smaller number, swap it into position 
            my_list[low] = my_list[high]
            
            # Now look for a number larger than the pivot point 
            while low < high and my_list[low] <= pivot:
                low += 1
                
            if low < high:
                # Found one! Move it into position 
                my_list[high] = my_list[low]
                
    # Move the pivot back into the list and return its index items[low] = pivot
    return low

# Example usage:
example_list = [33, 10, 59, 26, 41, 58, 18] 
sorted_list = quick_sort(example_list, 0, len(example_list) - 1) 
print(sorted_list)

print("\n--------------------------------------------------------\n")
