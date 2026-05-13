"""
----------------------------------------------

Lillia Lessev

Recursion

----------------------------------------------

"""

print("\n--------------------------------------------------------\n")


def largest_number(num_list):
    if len(num_list) == 1:
        result = num_list[0]
        return result
    else:
        length = len(num_list) - 1
        if (num_list[length] > num_list[length-1]):
            # largest = num_list[length]
            del num_list[length-1]
        elif (num_list[length] < num_list[length-1]):
            # largest = num_list[length-1]
            del num_list[length]
        return largest_number(num_list)


num_list = [345, 4893, 583, 987, 2345, 2546]

print(f"Result: {largest_number(num_list)}")

print("\n--------------------------------------------------------\n")