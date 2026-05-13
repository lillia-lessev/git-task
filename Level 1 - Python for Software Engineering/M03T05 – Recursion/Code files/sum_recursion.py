"""
----------------------------------------------

Lillia Lessev

Recursion

----------------------------------------------

"""

print("\n--------------------------------------------------------\n")

def sum(num_list, index):
    # Sum all nums in list from position 0 until and including specified index   
    if index <= 0:
        result = num_list[index] 
        return result
    else:
        result = num_list[index] + sum(num_list, (index-1))
        return result
    


num_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for index in range(len(num_list)):
    print(f"Result: {sum(num_list, index)}")



print("\n--------------------------------------------------------\n")