"""
----------------------------------------------

Lillia Lessev

Capstone Project: Task Manager


----------------------------------------------

"""



# ===== Importing external modules ===========
'''This is the section where you will import modules'''
from datetime import datetime
from tabulate import tabulate
from textwrap import wrap
import textwrap


# ==== Classes === 
class Task:
    """
    A class representing a task object
    
    Attributes:
        username (str): the username of the person assigned to the task
        title (str): the title of the task
        description (str): a description of the task
        date_assigned (str): the date the task was assigned to the user
        due_date (str): the date that the task is due
        completed (str): a 'Yes' or 'No' value depicting whether or not the task has been completed yet
    """
    
    def __init__(self, username, title, description, date_assigned, due_date, completed):
        """
        Initialise a task object

        Args:
            username (str): the username of the person assigned to the task
            title (str): the title of the task
            description (str): a description of the task
            date_assigned (str): the date the task was assigned to the user
            due_date (str): the date that the task is due
            completed (str): a 'Yes' or 'No' value depicting whether or not the task has been completed yet
        """
        # Username, Title, Description, Date_assigned, Due_date, Completed
        self.username = username
        self.title = title
        self.description = description
        self.date_assigned = date_assigned
        self.due_date = due_date
        self.completed = completed
    
    def get_user(self):
        """
        Returns the user assigned to a task

        Returns:
            (str): username of user assigned to the task
        """
        return self.username
    
    def get_title(self):
        """
        Returns the title of a task

        Returns:
            (str): title of the task
        """
        return self.title
    
    def get_description(self):
        """
        Returns the description of a task

        Returns:
            (str): description of the task
        """
        return self.description
    
    def get_date_assigned(self):
        """
        Returns the date a task as assigned

        Returns:
            (str): the assignment date of the task
        """
        return self.date_assigned
    
    def get_due_date(self):
        """
        Returns the due date a task 

        Returns:
            (str): the due date of the task
        """
        return self.due_date
    
    def get_completed(self):
        """
        Returns the completion status of a task

        Returns:
            (str): 'Yes' or 'No' value to depict whether or not a task has been completed yet
        """
        return self.completed
        
# === Other methods / functions ===
def read_users():
    """
    Reads all the users and passwords from the text file and returns them as a dictionary
    
    Returns:
        list: User details including usernames and passwords
    """
    
    user_details = {}
        
    # Reading data from file
    try:
        with open("user.txt", "r", encoding="utf-8") as file:
            for line in file:
                credentials = line
                split_cred = credentials.split(", ") # username, password
                username = split_cred[0]
                password = split_cred[1]
                user_details.update({username: password}) # Adds details to dictionary
    except FileNotFoundError:
        print("Error reading existing users from file.")

    return user_details

def check_user_exists(input_username):
    """
    Checks whether a username already exists in the test file of users.
    
    Returns:
        bool: a True or False value to determine if the username exists
    """
    
    user_already_exists = True
    user_dict = read_users()

    # Getting + Checking username 
    # while (user_already_exists == True):
    # input_username = input("Enter username: ")

    # Check if username exists
    for i in range(len(user_dict)):
        usernames = list(user_dict.keys())
        current_user = usernames[i]

        if current_user == input_username:
            # Username already exists
            user_already_exists = True
            break
        else:
            # Matching username not found
            user_already_exists = False

    return user_already_exists

def read_tasks():
    """
    Reads the tasks text file and collects the data / details about the tasks stored there
    
    Returns:
        list: a list of task objects containing the details of each task in the tasks text file
    """
    tasks_list = []
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                details = line
                split_details = details.split(", ") 
                
                # Username, Title, Description, Date_assigned, Due_date, Completed
                user = split_details[0]
                title = split_details[1]
                description = split_details[2]
                date_assigned = split_details[3]
                due_date = split_details[4]
                completed = split_details[5].strip('\n')

                current_task = Task(user, title, description, date_assigned, due_date, completed)
                tasks_list.append(current_task)
    except FileNotFoundError:
        print("Error reading existing users from file.")
    
    return tasks_list
    
# ==== Login Section ====
def login():
    """
    Allows user to login by checking whether the correct username and password has been entered.
    
    Returns:
        bool: True or False value to check whether or not the login was successful
    """
    success_login = False
    while success_login == False:
        
        print("\n--------------------------------------------------------\n")
        print("LOGIN")
        print("\n--------------------------------------------------------\n")
        current_username = input("Enter username: ")
        current_password = input("Enter password: ")
        user_match = False
        password_match = False
        username_list = []
        password_list = []
        
        # Reading data from file
        try:
            with open("user.txt", "r", encoding="utf-8") as file:
                for line in file:
                    credentials = line
                    split_cred = credentials.split(", ") # username, password
                    username = split_cred[0]
                    password = split_cred[1].strip('\n')
                    username_list.append(username)
                    password_list.append(password)
        except FileNotFoundError:
            print("Error reading existing users from file.")
        
        # Checking details
        for i in range(len(username_list)):
            if username_list[i] == current_username:
                # Username match found
                user_match = True

                if password_list[i] == current_password:
                    # Password match found
                    password_match = True
                    print("Successfully logged in.")
                    success_login = True
                    break
                else:
                    # Incorrect password
                    print("The password entered is incorrect.")
                    password_match = False
                    success_login = False
                    break
                
            else:
                user_match = False
        
        if user_match == False:
            # No matching username found
            print("Invalid user - user does not exist.")
            success_login = False
    login_details = [success_login, current_username]
    return login_details


# Calling up login view    
login_details = login()
login_successful = login_details[0]
user_logged_in = login_details[1]

# Bringing up menu if login was sucessful
while login_successful == True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    print("\n--------------------------------------------------------\n")
    print("MENU")
    print("\n--------------------------------------------------------\n")

    menu = input('''Select one of the following options and type ONLY the letter(s):\n
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit\nOption: ''').lower()

    # REGISTERING NEW USER
    if menu == 'r':

        user_already_exists = True
        pass_match = False

        user_dict = read_users()

        # Getting + Checking username 
        new_username = input("Enter username: ")
        user_already_exists = check_user_exists(new_username)
        while (user_already_exists == True):
            print("This username already exists. Please try a different one.")
            print("Please note that usernames are case-sensitive.")
            new_username = input("Enter username: ")
            user_already_exists = check_user_exists(new_username)
            
        # If user inputs unique username, proceed to setting password
        # Getting + Checking password
        while (pass_match == False) and (user_already_exists == False):
            # Entering passowrd
            new_password1 = input("Enter password: ")
            new_password2 = input("Please confirm password: ")

            # Checking if passwords match
            if new_password1 == new_password2:
                # Passwords match
                print("Password confirmed.")
                pass_match = True
                break
            else:
                # Passwords don't match
                print("Passwords do not match. Please try again.")
                pass_match = False
                
        # Storing new user details in text file
        try:
            with open("user.txt", "r+", encoding="utf-8") as file:
                file.seek(0, 2) # Sets position to end of file
                new_details = (f"\n{new_username}, {new_password1}")
                file.write(new_details)
                print("\nUsername and user password saved to text file.")
        except FileNotFoundError:
            print("Error saving new user details to file.")

    # ADDING NEW TASK
    elif menu == 'a':

        print("\nCREATING A NEW TASK:\n")
        # Username, Title, Description, Date_assigned, Due_date, Completed
        user = input("Enter username to whom task is assigned: ")
        user_exists = check_user_exists(user)
        while user_exists == False:
            print("Error. This username does not exist. Please type a valid, existing username.")
            user = input("Enter username to whom task is assigned: ")
            user_exists = check_user_exists(user)
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        
        # Validate assignment date
        date_assigned_option = None
        # day = None
        # month = None
        # year = None
        
        while (date_assigned_option != 1) and (date_assigned_option != 2):
            date_assigned_option = input("Which date is / was this task assigned?\nTyped the number ONLY from the options below:"
                                    + "\n1 - Today\n2 - Custom\nEnter option: ")
            try:
                date_assigned_option = int(date_assigned_option)
            except:
                print("Error. Option entered needs to be either only 1 or 2.")
            
            if date_assigned_option == 1:
                # Today
                date_assigned = datetime.now()
                day = int(date_assigned.strftime("%d"))
                month = int(date_assigned.strftime("%m"))
                year = int(date_assigned.strftime("%Y"))
                date_assigned = date_assigned.strftime("%d %b %Y") # Learnt about datetime from W3Schools (n.d.). Full reference at end of project.
                
                
            elif date_assigned_option == 2:
                print("Please enter the date assigned in the following format dd-mm-yyyy\ne.g. 31-12-2024")
                date_assigned = input("Enter date (dd-mm-yyy): ")
                date_split = date_assigned.split('-')
                day = int(date_split[0])
                month = int(date_split[1])
                year = int(date_split[2])
                date_assigned = datetime.strptime(date_assigned, "%d-%m-%Y")
                date_assigned = date_assigned.strftime("%d %b %Y")
            else:
                print("Invalid option. Please try again.")
        
        # Validate due date
        valid_due_date = False
        while (valid_due_date == False):
            try:
                print("Please enter the due date of the task in the following format dd-mm-yyyy\ne.g. 31-12-2024")
                due_date = input("Enter due date (dd-mm-yyy): ")
                due_date_split = due_date.split('-')
                due_day = int(due_date_split[0])
                due_month = int(due_date_split[1])
                due_year = int(due_date_split[2])
                
                if due_year < year: # Invalid year
                    valid_due_date = False
                    print("Error. Due date must be after assignment date.")
                elif due_year == year: # Valid year
        
                    if due_month < month: # Invalid due month
                        valid_due_date = False
                        print("Error. Due date month cannot be before the month of assignment.")
                    elif due_month == month: # Same month
                        if due_day < day: # invalid day - due date before assignent
                            valid_due_date = False
                            print("Error. Due date day cannot be before day of assignment.")
                        elif due_day >= day: # valid day
                            valid_due_date = True
                    elif due_month > month: # Valid month
                        valid_due_date = True
                elif due_year > year: # Valid year
                    valid_due_date = True

            except:
                print("Invalid due date entered. Please try again.")
                valid_due_date = False
        
        due_date = datetime.strptime(due_date, "%d-%m-%Y")
        due_date = due_date.strftime("%d %b %Y")
        
        completed = "No"
        print("Task saved as 'incomplete'.")
        
        # Username, Title, Description, Date_assigned, Due_date, Completed
        task_details_str = str(f"\n{user}, {title}, {description}, {date_assigned}, {due_date}, {completed}")
        
        try:
            # Writing to file
            with open("tasks.txt", "r+", encoding="utf-8") as file:
                file.seek(0, 2) # Sets cursor to end of file
                file.write(task_details_str)
        except FileNotFoundError:
            print("Error writing new task to file.")

    elif menu == 'va':

        task_list = []
        task_list = read_tasks()
        table_data = []
        
        
        for task in range(len(task_list)):
            # Username, Title, Description, Date_assigned, Due_date, Completed
            task_object = task_list[task]
            user = task_object.get_user()
            
            title = task_object.get_title()
            title = textwrap.wrap(title, width=20)
            title_str = ""
            for wrap in range(len(title)):
                title_str = title_str + title[wrap] + "\n"
            
            
            description = task_object.get_description()
            description = textwrap.wrap(description, width=20)
            desc_str = ""
            for wraps in range(len(description)):
                desc_str = desc_str + description[wraps] + "\n"
                wraps += 1
            
            date_assigned = task_object.get_date_assigned()
            due_date = task_object.get_due_date()
            completed = task_object.get_completed()
            
            table_data.append([(task + 1), user, title_str, desc_str, date_assigned, due_date, completed])
            task +=1
        
        
        table_headers = ["Task\nno.", "Username of user\nassigned to task", "Task Title", "Task Description", "Date Assigned", "Due Date", "Has task been\nCompleted?"]
        table = tabulate(table_data, headers=table_headers, tablefmt="grid", maxcolwidths=[None, 10])
        print("\n------ ALL TASK DETAILS ------\n")
        print(table)

    elif menu == 'vm':
    
        task_list = []
        task_list = read_tasks()
        table_data = []
        
        
        for task in range(len(task_list)):
            # Username, Title, Description, Date_assigned, Due_date, Completed
            task_object = task_list[task]
            user = task_object.get_user()
            if user == user_logged_in:
                title = task_object.get_title()
                title = textwrap.wrap(title, width=20)
                title_str = ""
                for wrap in range(len(title)):
                    title_str = title_str + title[wrap] + "\n"
                
                
                description = task_object.get_description()
                description = textwrap.wrap(description, width=20)
                desc_str = ""
                for wraps in range(len(description)):
                    desc_str = desc_str + description[wraps] + "\n"
                    wraps += 1
                
                date_assigned = task_object.get_date_assigned()
                due_date = task_object.get_due_date()
                completed = task_object.get_completed()
                
                table_data.append([user, title_str, desc_str, date_assigned, due_date, completed])
            else:
                pass
            task +=1
            
        if len(table_data) < 1:
            print("\nYou currently have no tasks.")
        elif len(table_data) >= 1:
            table_headers = ["Username of user\nassigned to task", "Task Title", "Task Description", "Date Assigned", "Due Date", "Has task been\nCompleted?"]
            table = tabulate(table_data, headers=table_headers, tablefmt="grid", maxcolwidths=[None, 10])
            print("\n------ MY TASK DETAILS ------\n")
            print(table)

    elif menu == 'e':
        print("\nGoodbye!\n")
        login_successful == False
        exit()

    else:
        print("You have entered an invalid input.",
              "\nPlease only enter one of letters from the options and try again")
        
        
        


"""
-------------------------
REFERNCES (APA 7 Style)

W3Schools. (n.d.). Python Dates. Www.w3schools.com. https://www.w3schools.com/python/python_datetime.asp 
"""
