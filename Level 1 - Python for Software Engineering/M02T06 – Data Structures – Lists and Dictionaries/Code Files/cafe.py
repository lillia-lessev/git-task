"""
----------------------------------------------

Lillia Lessev

Data Structures - Lists and Dictionaries


----------------------------------------------

"""

print("\n--------------------------------------------------------\n")

total_stock = 0.0
i = 0

menu = ["Burger", "Chips", "Milkshake", "Cake"]
stock = {0: 50, 1: 50, 2: 50, 3: 20} # How much is in stock
price = {0: 150, 1: 35, 2: 50, 3: 35}

for food in menu:
    total_stock = total_stock + (price.get(i) * stock.get(i))
    i+=1
    
print(f"The total worth of the stock is: {total_stock}")




print("\n--------------------------------------------------------\n")
