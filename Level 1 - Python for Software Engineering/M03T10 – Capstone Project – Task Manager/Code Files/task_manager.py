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
    
    def __str__(self):
        """
        Returns a string representation of a Task object.

        Returns:
            str: A string representation of a Task object in the format of a table
        """
        
        table_data = []
        
        user = self.username
        
        title = self.title
        title = textwrap.wrap(title, width=20)
        title_str = ""
        for wrap in range(len(title)):
            title_str = title_str + title[wrap] + "\n"
        
        description = self.description
        description = textwrap.wrap(description, width=20)
        desc_str = ""
        for wraps in range(len(description)):
            desc_str = desc_str + description[wraps] + "\n"
            wraps += 1
        
        date_assigned = self.date_assigned
        due_date = self.due_date
        completed = self.completed
        
        table_data.append([user, title_str, desc_str, date_assigned, due_date, completed])
        table_headers = ["Task\nno.", "Username of user\nassigned to task", "Task Title", "Task Description", "Date Assigned", "Due Date", "Has task been\nCompleted?"]
        table = tabulate(table_data, headers=table_headers, tablefmt="grid", maxcolwidths=[None, 10])
        
        return table
        
        
    
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

def reg_user():
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

def add_task():
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

def view_all_tasks():
    """
    Displays all tasks, for all users in the task.txt text file and displays them in the format of a table.
    """
    
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

def view_mine():
    """
    Returns a list of all the tasks for the specified user and
        displays the tasks marked as 'completed' ("Yes") in the task.txt text file for the specific user in the format of a table.
        
    Returns:
        (list): a list of the tasks assigned to the specific user logged in 
    """
    task_list = []
    task_list = read_tasks()
    table_data = []
    task_num = 0
    my_tasks = []
    
    
    for task in range(len(task_list)):
        # Username, Title, Description, Date_assigned, Due_date, Completed
        task_object = task_list[task]
        user = task_object.get_user()
        if user == user_logged_in:
            task_num = task_num + 1
            title = task_object.get_title()
            title_wrap = textwrap.wrap(title, width=20)
            title_str = ""
            for wrap in range(len(title_wrap)):
                title_str = title_str + title_wrap[wrap] + "\n"
            
            
            description = task_object.get_description()
            description_wrap = textwrap.wrap(description, width=20)
            desc_str = ""
            for wraps in range(len(description_wrap)):
                desc_str = desc_str + description_wrap[wraps] + "\n"
                wraps += 1
            
            date_assigned = task_object.get_date_assigned()
            due_date = task_object.get_due_date()
            completed = task_object.get_completed()
            
            my_task = Task(user,title, description, date_assigned, due_date, completed)
            my_tasks.append(my_task)
            
            table_data.append([task_num, user, title_str, desc_str, date_assigned, due_date, completed])
        else:
            pass
        task +=1
        
    if len(table_data) < 1:
        print("\nYou currently have no tasks.")
    elif len(table_data) >= 1:
        table_headers = ["Task no.", "Username of user\nassigned to task", "Task Title", "Task Description", "Date Assigned", "Due Date", "Has task been\nCompleted?"]
        table = tabulate(table_data, headers=table_headers, tablefmt="grid", maxcolwidths=[None, 10])
        print("\n------ MY TASK DETAILS ------\n")
        print(table)
        
    
    return my_tasks

def view_completed():
    """
    Displays all tasks marked as 'completed' ("Yes") in the task.txt text file in the format of a table.
    """
    
    task_list = []
    task_list = read_tasks()
    table_data = []
    
    
    
    for task in range(len(task_list)):
        # Username, Title, Description, Date_assigned, Due_date, Completed
        task_object = task_list[task]
        user = task_object.get_user()
        
        title = task_object.get_title()
        title_wrap = textwrap.wrap(title, width=20)
        title_str = ""
        for wrap in range(len(title_wrap)):
            title_str = title_str + title[wrap] + "\n"
        
        
        description = task_object.get_description()
        description_wrap = textwrap.wrap(description, width=20)
        desc_str = ""
        for wraps in range(len(description_wrap)):
            desc_str = desc_str + description_wrap[wraps] + "\n"
            wraps += 1
        
        date_assigned = task_object.get_date_assigned()
        due_date = task_object.get_due_date()
        completed = task_object.get_completed()
        
        
        
        if completed == "Yes":
            table_data.append([(task + 1), user, title_str, desc_str, date_assigned, due_date, completed])
        elif completed == "No":
            pass
        task +=1
    
    if len(table_data) < 1:
        print("\nThere are currently no tasks which have been completed.")
    elif len(table_data) >= 1:
        table_headers = ["Username of user\nassigned to task", "Task Title", "Task Description", "Date Assigned", "Due Date", "Has task been\nCompleted?"]
        table = tabulate(table_data, headers=table_headers, tablefmt="grid", maxcolwidths=[None, 15])
        print("\n------ COMPLETED TASKS ------\n")
        print(table)
    
def delete_task(task_no):
    """
    Deletes selected task from tasks.txt
    """
    
    num = 0
    lines = []
    
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                if num == task_no:
                    pass
                elif num != task_no:
                    details = line
                    lines.append(details)
                num += 1
    except FileNotFoundError:
        print("Error reading existing tasks from file.")
        
    try:
        with open("tasks.txt", "w", encoding="utf-8") as file:
            file.seek(0,0)
            for j in range(len(lines)):
                if j == (len(lines) - 1):
                    task_details = lines[j]
                    task_details = task_details.strip("\n")
                    lines[j] = task_details
                    file.write(lines[j])
                else:
                    file.write(lines[j])
                j += 1
                
    except FileNotFoundError:
        print("Error writing updated task list to file.")    

def edit_task(selected_task, edit_option):
    task_list = []
    task_list = read_tasks()
    
    if edit_option == 1:
        edit_user = True
        edit_due_date = False
    elif edit_option == 2:
        edit_user = False
        edit_due_date = True
    elif edit_option == 3:
        edit_user = True
        edit_due_date = True
    
    # EDIT USER
    if edit_user == True:
        i = 0 
        for i in range(len(task_list)):
            task_in_list = task_list[i]
            task_in_list_str = str(task_in_list)
            
            user_task = selected_task
            user_task_str = str(user_task)
            
            if task_in_list_str == user_task_str:
                # Edit task
                # Username, Title, Description, Date_assigned, Due_date, Completed
                task_no = i
                user_exists = False
                while user_exists == False:
                    print("--- Editing username ---")
                    username = input("Enter new username: ")
                    user_exists = check_user_exists(username)
                    if user_exists == False:
                        print("Error. User does not exist. Please choose an existing username.")
                    elif user_exists == True:
                        title = task_in_list.get_title()
                        description = task_in_list.get_description()
                        date_assigned = task_in_list.get_date_assigned()
                        due_date = task_in_list.get_due_date()
                        completed = task_in_list.get_completed()
                        edited_task = Task(username, title, description, date_assigned, due_date, completed)
                        task_list[i] = edited_task

                        if edit_option == 3:
                            user_task = edited_task
            else:
                pass
            
            i += 1
    
    
        
    
    # EDIT DUE DATE
    if edit_due_date == True:
        print("--- Editing Due Date ---")
        i = 0
        for i in range(len(task_list)):
            task_in_list = task_list[i]
            task_in_list_str = str(task_in_list)
            
            if edit_option == 3:
                user_task = edited_task
            else:
                user_task = selected_task
            
            user_task_str = str(user_task)
            
            if task_in_list_str == user_task_str:
                # Edit task
                # Username, Title, Description, Date_assigned, Due_date, Completed
                # user_task = selected_task
                date_assigned = task_in_list.get_date_assigned()
                split_date = date_assigned.split(" ")
                day = split_date[0]
                day = int(day)
                month = split_date[1]
                try:
                    month = datetime.strptime(month, "%b")
                    month = month.strftime("%m")
                    month = int(month)
                except:
                    print("Error getting month.")
                year = split_date[2]
                year = int(year)
                
                # try:
                #     due_date = datetime.strptime(due_date, "%d-%m-%Y")
                #     due_date = due_date.strftime("%d %b %Y")
                # except:
                #     print("Error changing due date.")
                
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
                
                username = task_in_list.get_user()
                title = task_in_list.get_title()
                description = task_in_list.get_description()
                date_assigned = task_in_list.get_date_assigned()
                # due_date = task_in_list.get_due_date()
                completed = task_in_list.get_completed()
                edited_task = Task(username, title, description, date_assigned, due_date, completed)
                task_list[i] = edited_task
            
            else:
                pass
            
            i += 1
    
    # Adding edits to text file
        
    try:
        with open("tasks.txt", "w+", encoding="utf-8") as file:
            file.seek(0,0)
            
            for j in range(len(task_list)):
                if j == (len(task_list) - 1):
                    current_task = task_list[j]
                    user = current_task.get_user()
                    title = current_task.get_title()
                    description = current_task.get_description()
                    date_assigned = current_task.get_date_assigned()
                    due_date = current_task.get_due_date()
                    completed = current_task.get_completed()
                    completed = completed.strip("\n")
                    
                    task_details_str = str(f"{user}, {title}, {description}, {date_assigned}, {due_date}, {completed}")
                
                    file.write(task_details_str)
                    
                else:
                    # Username, Title, Description, Date_assigned, Due_date, Completed
                    current_task = task_list[j]
                    user = current_task.get_user()
                    title = current_task.get_title()
                    description = current_task.get_description()
                    date_assigned = current_task.get_date_assigned()
                    due_date = current_task.get_due_date()
                    completed = current_task.get_completed()
                    
                    task_details_str = str(f"{user}, {title}, {description}, {date_assigned}, {due_date}, {completed}\n")
                    
                    file.write(task_details_str)
                
                j += 1
                
    except FileNotFoundError:
        print("Error writing updated task list to file.")    
    
    

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

    if user_logged_in == "admin":
        menu = input('''Select one of the following options and type ONLY the letter(s):\n
            r - register a user
            a - add task
            va - view all tasks
            vm - view my tasks
            vc - view completed tasks
            del - delete tasks
            e - exit\nOption: ''').lower()
    
    elif user_logged_in != "admin":
        menu = input('''Select one of the following options and type ONLY the letter(s):\n
            a - add task
            va - view all tasks
            vm - view my tasks
            e - exit\nOption: ''').lower()

    # REGISTERING NEW USER - option for admin only
    if (menu == 'r') and (user_logged_in == "admin"):
        reg_user()

    # ADDING NEW TASK
    elif menu == 'a':
        add_task()

    # VIEWING ALL TASKS
    elif menu == 'va':
        view_all_tasks()

    # VIEWING MY TASKS
    elif menu == 'vm':
        my_tasks = []
        my_tasks = view_mine()
        if (len(my_tasks) - 1) >= 0:
            
            
            
            valid_option = False


            
            while valid_option == False:
                is_int = False
                while is_int == False:
                    print("\nSelect a task to edit it by typing the task number ONLY and press ENTER.")
                    print("Type   -1   to go back to the main menu.")
                    print("Please note: You cannot edit tasks which have already been completed.")
                    print("\nPlease enter either a task number or  -1.")
                    
                    try:
                        option = input("Input: ")
                        option = int(option)
                        if isinstance(option, int):
                            is_int = True
                        elif not isinstance(option, int):
                            is_int = False
                    except ValueError:
                        print("Error. Please enter a NUMBER ONLY and press ENTER.")
                
                if option == -1:
                    valid_option = True
                    break
                elif (option > len(my_tasks)) or option < 1:
                    print("Error. Invalid option.")
                elif (option <= len(my_tasks) and option > 0):
                    selected_task = my_tasks[option-1]
                    completed = selected_task.get_completed()
                    if completed == "No":
                        is_int = False
                        valid_edit_option = False
                        while is_int == False or valid_edit_option == False:
                            print('''Please select the detail you'd like to edit and type the option NUMBER ONLY:\n
                            1 - Edit user
                            2 - Edit due date
                            3 - Edit both the user and the due date''')
                        
                            try:
                                edit_option = input("Option: ")
                                edit_option = int(edit_option)
                                if isinstance(edit_option, int):
                                    is_int = True
                                    # EDIT USER
                                    if edit_option == 1:
                                        edit_task(selected_task, 1)
                                        print("User edited.")
                                        valid_edit_option = True
                                    
                                    # EDIT DUE DATE
                                    elif edit_option == 2:
                                        edit_task(selected_task, 2)
                                        print("Due date edited.")
                                        valid_edit_option = True
                                    
                                    # EDIT BOTH
                                    elif edit_option == 3:
                                        edit_task(selected_task, 3)
                                        print("User and due date edited.")
                                        valid_edit_option = True

                                    else:
                                        print("Invalid option.")
                                        valid_edit_option = False
                                
                                elif not isinstance(edit_option, int):
                                    is_int = False
                            except ValueError:
                                print("Error. Please choose an option from the list. Enter a NUMBER ONLY and press ENTER.")

                            
                        
                        
                        valid_option = True
                    elif completed == "Yes":
                        valid_option = False
                        print("You cannot edit a task that's already been completed.")
                    else:
                        print("Error. Invalid option selected.")
                        break
                        
                    
            
        else:
            print("There are no tasks to view or edit.")

    # VIEW COMPLETED TASKS - option for admin user only
    elif (menu == 'vc') and (user_logged_in == "admin"):
        view_completed()
    
    # DELETE TASKS - option for admin user only
    elif (menu == 'del') and (user_logged_in == "admin"):

        deleting_task = True
        while deleting_task == True:
            view_all_tasks()
            task_list = []
            task_list = read_tasks()
            valid_option = False
            is_int = False

            while is_int == False:
                print("\nAll tasks currently being stored have been displayed in the table above.")
                print("Please type the 'Task no.' of the task you'd like to delete (NUMBER ONLY).")
                try:
                    task_no = input("Task number: ")
                    task_no = int(task_no)
                    if isinstance(task_no, int):
                        is_int = True
                    elif not isinstance(task_no, int):
                        is_int = False
                except ValueError:
                    print("Error. Please enter the task NUMBER ONLY as an integer and press ENTER.")
            
            while valid_option == False:
                if (task_no > len(task_list)) or task_no < 1:
                    print("Error. Please enter a valid task number.")
                    break
                elif (task_no <= len(task_list) and task_no > 0):
                    task_no = task_no - 1
                    task = task_list[task_no]
                    print(str(task))
                    print("Are you sure you want to delete this task?.")
                    option = input("y/n: ").lower()
                    if option == "y":
                        delete_task(task_no)
                        print("Task deleted.")
                        deleting_task = False
                        valid_option = True
                        break
                    elif option == "n":
                        print("Task has NOT been deleted.")
                        deleting_task = False
                        valid_option = True
                        break
                else:
                    print("Error. Invalid input.")
                    break

    # EXIT PROGRAM
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
