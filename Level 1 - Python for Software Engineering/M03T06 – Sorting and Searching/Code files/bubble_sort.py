"""
----------------------------------------------

Lillia Lessev

Abstract Data Types

----------------------------------------------

"""

print("\n--------------------------------------------------------\n")


def bubble_sort(items):
    # Traverse through all elements in the list 
    for i in range(len(items) - 1, -1, -1):
        # Traverse the list from 1 to i
        for j in range(1, i + 1):
            # Swap if the element is greater than the next element 
            item_a = items[j - 1]
            item_b = items[j]
            #if items[j - 1] > items[j]:
            if item_a > item_b:
                #items[j - 1], items[j] = items[j], items[j - 1]
                items[j - 1], items[j] = item_b, item_a
    return items

# Example usage: 
example_list = [8, 3, 2, 6, 7, 4, 11, 5] 
sorted_list = bubble_sort(example_list) 
print(sorted_list)

print("\n--------------------------------------------------------\n")
