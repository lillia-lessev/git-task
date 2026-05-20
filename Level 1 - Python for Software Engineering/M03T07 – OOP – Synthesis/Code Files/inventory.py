"""
----------------------------------------------

Lillia Lessev

OOP - Synthesis

----------------------------------------------

"""
# Importing relevant modules
from tabulate import tabulate

# Checking Working directory for debugging
# import os
# print("\n\nCurrent working dir: ", os.getcwd())


# ========The beginning of the class==========
class Shoe:
    """
    A class representing a shoe product / object

    Attributes:
        country (str): Country the shoe is from
        code (str): the unique code identifying the shoe
        product (str): the specific name of the shoe
        cost (int): how much the shoe costs
        quantity (int): how many shoes are in stock
    """

    # Constructor Method
    # Country,Code,Product,Cost,Quantity
    def __init__(self, country, code, product, cost, quantity):
        """
        Initialise a Shoe object.

        Args:
            country (str): Country the shoe is from
            code (str): the unique code identifying the shoe
            product (str): the specific name of the shoe
            cost (int): how much the shoe costs
            quantity (int): how many shoes are in stock
        """

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_country(self):
        """
        Returns the country of the shoe.

        Returns:
            str: The code of the shoe object.
        """
        return self.country

    def get_code(self):
        """
        Returns the coountry of the shoe.

        Returns:
            str: The code of the shoe object.
        """
        return self.code

    def get_product(self):
        """
        Returns the product name of the shoe.

        Returns:
            str: The product name of the shoe object.
        """
        return self.product

    def get_cost(self):
        """
        Returns the cost of the shoe.

        Returns:
            int: The cost number of the shoe object.
        """
        return self.cost

    def get_quantity(self):
        """
        Returns the quantity of the shoe in stock.

        Returns:
            int: The number of shoe objects in stock.
        """
        return self.quantity

    def __str__(self):
        """
        Returns a string representation of a Shoe object.

        Returns:
            str: A string representation in the format
                Shoe details:

                Product:    product
                Code:       code
                Country:    country
                Cost:       cost
                Quantity:   quantity
        """
        shoe_str = (f'''Shoe details:\n\nProduct:\t{self.product}\nCode:\t\t{self.code}\nCountry:\t{self.country}\nCost:\t\t{self.cost}\nQuantity:\t{self.quantity}''')
        return shoe_str

# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

# ==========Functions outside the class==============
# READING SHOE DATA
def read_shoes_data():
    """
    Read shoe data from text file and append it to shoe_list as a Shoe object.

    Returns:
        list: A list containing shoe objects

    """

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

    try:
        with open("inventory.txt", "r+", encoding="utf-8") as file:
            i = 0
            shoe_list = []
            for line in file:

                # Skipping first line (header line) in text file
                if (i <= 0):
                    pass
                elif (i > 0):

                    details_line = line
                    split_details = details_line.split(',')  # Country,Code,Product,Cost,Quantity

                    try:
                        country = split_details[0]
                        code = split_details[1]
                        product = split_details[2]
                        cost = split_details[3]
                        cost = int(cost)
                        quantity = split_details[4]
                        quantity = int(quantity)

                        shoe = Shoe(country, code, product, cost, quantity)
                        shoe_list.append(shoe)
                    except:
                        print("Error reading details from text file, creating new shoe object and appending 1it to list.")

                i += 1
    except FileNotFoundError:
        print("The file that you trying to open does not exist. Please check the file path and try again.\n")

    return shoe_list

# CAPTURING AND STORING DATA ABOUT SHOE OBJECT
def capture_shoes():
    """
    Use data to create a new Shoe object and append it to the shoe_list.
    """

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

    # Getting details for new shoe object
    try:

        print("Please input the deatils for the shoe and press ENTER after each item.")
        country = str(input("Enter country: "))
        code = str(input("Enter product code: ")).upper()
        product = str(input("Enter the product name: "))
        cost_int = False
        while cost_int == False:
            try:
                print("Please enter the cost of the shoe as an INTEGER ONLY. No currency symbols or decimal points.")
                cost = int(input("Enter cost: "))
                if isinstance(cost, int):
                    cost_int = True
                elif not isinstance(cost, int):
                    cost_int = False
            except TypeError:
                print("Error entering cost. Cost needs to be an integer.")
        quantity_int = False
        while quantity_int == False:
            try:
                print("Please enter the stock quantity of the shoe as an INTEGER ONLY. No decimal points.")
                quantity = int(input("Enter quantity: "))
                if isinstance(quantity, int):
                    quantity_int = True
                    break
                elif not isinstance(quantity, int):
                    quantity_int = False
            except TypeError:
                print("Error entering quantity. Quantity needs to be an integer.")          
    except:    
        print("Error capturing shoe details.")

    # Adding new shoe details to text file
    # Country,Code,Product,Cost,Quantity
    try:
        with open("inventory.txt", "r+", encoding="utf-8") as file:
            file.seek(0, 2)  # This means move the cursor 0 bytes from the end of the file. Learnt about seek() function from GeeksfroGeeks (2019). Full reference in reference list at the end of project. 
            shoe_line = (f"\n{country},{code},{product},{cost},{quantity}")
            file.write(shoe_line)
            # file.write(f"\n{country},{code},{product},{quantity}")
    except FileNotFoundError:
        print("Error writing new shoes to file.")

# DISPLAYING DATA FOR ALL SHOES
def view_all():

    """
    Display details for all shoe objects in the shoe_list.
    """

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python's tabulate module.
    '''

    # Getting shoe data from text file and storing shoe objects in shoe list
    shoe_list = read_shoes_data()

    # Looping over shoe list to print details for each shoe object
    # Learnt about tabulate from Astanin (2022). Full reference in reference list at end of project
    table_headers = ["Country", "Code", "Product", "Cost", "Quantity"]  # Country,Code,Product,Cost,Quantity
    table_data = []

    for i in range(len(shoe_list)):
        current_shoe = shoe_list[i]
        table_data.append([current_shoe.get_country(), current_shoe.get_code(), current_shoe.get_product(), current_shoe.get_cost(), current_shoe.get_quantity()])  # Country,Code,Product,Cost,Quantity
    table = tabulate(table_data, headers=table_headers, tablefmt="grid")
    print(table)

# RESTOCKING LOWEST QUANTITY SHOE
def re_stock():
    """
    Finds the shoe object with the lowest quantity.
    The user is asked if they want to restock the shoes, and the quantity is made larger.
    The new quantity is updated and stored in both the shoe_list with shoe objects and in the inventory.txt text file.

    """

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    shoe_list = read_shoes_data()
    shoe_list.sort(key=lambda shoe: shoe.get_quantity())
    low_shoe = shoe_list[0]
    lowest_quantity = low_shoe.get_quantity()

    print(f"The shoe with the lowest quantity is:\n{low_shoe}")
    print("\nWould you like to restock it?\nPlease choose your option below and type ONLY the number of your selection and press ENTER.")
    print("\n1 - Yes, I would like to restock the shoe.\n2 - No, I don't want to restock the shoe")
    option = None
    while option != 1 and option != 2:
        try:
            option = int(input("\nSelected option: "))
        except:
            print("Error. Please type only the number 1 or 2 based on your selection.")

        # Restock
        if (option == 1):
            # Restock list
            try:

                low_shoe_index = shoe_list.index(low_shoe)
                current_shoe = shoe_list[low_shoe_index]

                # Country,Code,Product,Cost,Quantity
                current_country = current_shoe.get_country()
                current_code = current_shoe.get_code()
                current_product = current_shoe.get_product()
                current_cost = current_shoe.get_cost()
                restock_quantity = lowest_quantity + 30

                current_shoe = Shoe(current_country, current_code, current_product, current_cost, restock_quantity)
                shoe_list[low_shoe_index] = current_shoe
            except:
                print("Error restocking shoe in shoe list.")

            # Restock text file
            try:
                with open("inventory.txt", "r+", encoding="utf-8") as file:
                    i = 0
                    file_lines = []
                    for line in file:
                        # Skipping first line (header line) in text file
                        if (i <= 0):
                            file.seek(0, 0)
                            file_lines.append(file.readline())
                        elif (i > 0):

                            details_line = line
                            split_details = details_line.split(',')  # Country,Code,Product,Cost,Quantity

                            country = split_details[0]
                            code = split_details[1]
                            product = split_details[2]
                            cost = split_details[3]
                            quantity = split_details[4]

                            # Checking for match: which product is being restocked? Which line needs to be altered?
                            try:
                                """
                                Checking which line in text file needs to be altered to reflect restock.
                                For good measure, I checked that the line contains both the code AND the product name I want to restock
                                    because if, for example, all the product codes aren't the same length and there happens to be a cpde which contains
                                    the same values as another code, the condition below will pick it up as a matching code even though it is not the code I am looking for.
                                    e.g. if one shoe has the code SKU123, another SKU12, another SKU, and another SKU12345
                                    and the user wants to restock 'SKU', the condition below will pick up 'SKU' in ALL of those lines.
                                    Therefore, I included the product name in the condition to make sure it is restocking the correct product.
                                """

                                if current_code and current_product in line:
                                    # Shoe match found
                                    quantity = restock_quantity
                                    new_str = (f"{country},{code},{product},{cost},{quantity}\n")
                                    file_lines.append(new_str)
                                    print("Shoe restocked and changes saved to text file.")
                                else:
                                    file_lines.append(line)
                            except:
                                print("Error restocking shoe and writing changes to text file.")
                        i += 1

                # Rewriting altered data back into text file.
                with open("inventory.txt", "r+", encoding="utf-8") as file:
                    file.seek(0, 0)
                    for j in range(len(file_lines)):
                        current_line = file_lines[j]
                        file.writelines(str(current_line))
            except FileNotFoundError:
                print("Error. The new quantity could not be written to the file. Please try again.")

        elif (option == 2):
            print("You have chosen not to restock the shoe.")

        else:
            print("Please choose a valid option")


# SEARCHING SHOE CODE AND DISPLAYING DETAILS
def search_shoe():
    """
    Searches for specified shoe object from the shoe_list using the unique shoe_code
    and displays the details of the shoe object.

    """

    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''

    # Populating shoe_list
    shoe_list = []
    shoe_list = read_shoes_data()

    code_match = False
    while code_match == False:
        print("Input shoe code and press ENTER.")
        shoe_code = str(input("Enter shoe code: "))
        for i in range(len(shoe_list)):
            current_shoe = shoe_list[i]
            current_code = current_shoe.get_code()
            if current_code == shoe_code:
                code_match = True
                print(str(current_shoe))
                break
            elif current_code != shoe_code:
                code_match = False

# CALCULATING TOTAL VALUE FOR SHOES
def value_per_item():
    """
    The total value of each shoe is calculated and displayed using the formula:
        total value = cost * quantity
    """

    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    shoe_list = []
    shoe_list = read_shoes_data()

    print("Total value for each shoe:\n")

    # Getting data and calculating total value
    for i in range(len(shoe_list)):
        current_shoe = shoe_list[i]
        current_quantity = current_shoe.get_quantity()
        current_cost = current_shoe.get_cost()
        total_value = current_cost * current_quantity
        print(str(current_shoe))
        print(str(f"Total value:\t{total_value}\n"))

# GETTING SHOE WITH HIGHEST QUANTITY
def highest_qty():
    """
    Retrieving the shoe object with the highest quantity and displaying it.
    """

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    shoe_list = []
    shoe_list = read_shoes_data()
    shoe_list.sort(key=lambda shoe: shoe.get_quantity())

    length = len(shoe_list) - 1
    high_shoe = shoe_list[length]
    print("The following shoe has the highest quantity and is for sale.")
    print(str(high_shoe))

# ==========Main Menu=============


"""
The main menu executes each function above and allows the user to select what they want to do.
"""

running = True
print("\nWELCOME!")
while running == True:
    print("\n--------------------------------------------------------\n")
    print("Shoe Inventory Program")
    print("\n--------------------------------------------------------\n")
    print("Please see the options in the menu below.")
    print("Select your option by typing ONLY the number and pressing ENTER.")
    print('''
          1 - View all shoes in stock
          2 - Capture data about a new shoe
          3 - Restock shoe with the lowest quantity in stock
          4 - Search for a specific shoe using its unique product code
          5 - Show the total value of each shoe (cost x quantity)
          6 - Show the shoe with the highest quantity in stock
          7 - Quit Program''')

    # Initialise Option
    option = None

    try:
        option = int(input("\nEnter option: "))
    except:
        print("Error. Invalid option. Please choose an option from the given list.\nType the number ONLY and press ENTER.")
    if option == 1:
        view_all()
    elif option == 2:
        capture_shoes()
    elif option == 3:
        re_stock()
    elif option == 4:
        search_shoe()
    elif option == 5:
        value_per_item()
    elif option == 6:
        highest_qty()
    elif option == 7:
        running = False
    else:
        print("Invalid option. Please try again.")

else:
    print("Quitting program.")
    print("Thank you for using the Shoe Inventory Program.")

print("\n--------------------------------------------------------\n")


"""
--- REFERENCES --- APA 7 Style

Astanin, S. (2022, October 6). tabulate: Pretty-print tabular data. PyPI. https://pypi.org/project/tabulate/ 

GeeksforGeeks. (2019, December 17). seek() function in Python. GeeksforGeeks. https://www.geeksforgeeks.org/python/python-seek-function/ 
"""
