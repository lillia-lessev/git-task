"""
----------------------------------------------

Lillia Lessev

Programming With Built-In Functions

----------------------------------------------

"""

#import statistics
from statistics import mean, median

print("\n--------------------------------------------------------\n")

num = 0
num_list = []
total = 0
max_num = 0
max_num_index = 0
min_num = 0
min_num_index = 0
avg = 0
med = 0

#GETTING NUMBERS
for i in range(0, 10):
    num = float(input("Please input a float / decimal number (. not ,): "))
    num_list.append(num)
    # total = total + num


#TOTAL
total = sum(num_list)
    
#AVERAGE
avg = mean(num_list)
avg = round(avg, 2)

#MAX
max_num = max(num_list)
max_num_index = num_list.index(max_num)

#MIN
min_num = min(num_list)
min_num_index = num_list.index(min_num)

#MEDIAN
med = median(num_list)

#DISPLAYING RESULTS
print(f"The total is: {total}")
print(f"The average is: {avg}")
print(f"The max is: {max_num} and the index is: {max_num_index}")
print(f"The min is: {min_num} and the index is: {min_num_index}")
print(f"The median is: {med}")


print("\n--------------------------------------------------------\n")
