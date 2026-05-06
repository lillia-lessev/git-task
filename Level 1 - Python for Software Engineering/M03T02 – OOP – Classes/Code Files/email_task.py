"""
----------------------------------------------

Lillia Lessev

OOP - Classes


----------------------------------------------

"""
"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

print("\n--------------------------------------------------------\n")


# --- OOP Email Simulator --- #

#-------------------------------------------------------------------------------------------------------------------#

# --------- Email Class -------------- #
# Create the class, constructor and methods to create a new Email object.

class Email:  

    
    # Initialise the instance variables for each email.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
        
    # Create the 'mark_as_read()' method to change the 'has_been_read' instance variable for a specific object from False to True.
    def mark_as_read(self):
        self.has_been_read = True

    # --- Functions --- #
    # Build out the required functions for your program.

# END OF Email CLASS #

#-------------------------------------------------------------------------------------------------------------------#

#------- FUNCTIONS FOR PROGRAM ----------#

# POPULATE INBOX FUNCTION #
def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    
    address_1 = "person1@gmail.com"
    address_2 = "person2@gmail.com"
    address_3 = "person3@gmail.com"
    
    subject_1 = "Attatchments"
    subject_2 = "Available times"
    subject_3 = "Thank you"
    
    message_1 = "Good day,\n\nPlease see attatched files.\n\nKind regards,\nLillia."
    message_2 = "Good day,\n\nPlease reply with available times.\n\nKind regards,\nLillia."
    message_3 = "Good day,\n\nThank you for your response.\n\nKind regards,\nLillia."

    email_1 = Email(address_1, subject_1, message_1)
    email_2 = Email(address_2, subject_2, message_2)
    email_3 = Email(address_3, subject_3, message_3)

    
    emails_list = [email_1, email_2, email_3]

    inbox.extend(emails_list)

# END OF POPULATE INBOX FUNCTION #

#-------------------------------------------------------------------------------------------------------------------#

# LIST EMAILS FUNCTION #
def list_emails():
    # Create a function that prints each email's subject line alongside its corresponding index number, regardless of whether the email has been read.
    print("Inbox:\n")
    for i, email in enumerate(inbox):
        print(f"{i}, {email.subject_line}")

# END OF LIST EMAILS FUNCTION #

#-------------------------------------------------------------------------------------------------------------------#

# READ EMAILS FUNCTION #
def read_email(index):
    # Create a function that displays the email_address, subject_line, and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method to set its 'has_been_read' instance variable to True.
    
    if (index >= 0) and (index <= len(inbox)):
        #index = int(input("Please input email index you want to read: "))
        selected_email = inbox[index] # selected_email is an email object
        print(f"\nFrom: {selected_email.email_address}")
        print(f"Subject: {selected_email.subject_line}")
        print(f"Content:\n\n{selected_email.email_content}\n\n")
    
        if selected_email != True:
            selected_email.mark_as_read()
            print(f"\nEmail from {selected_email.email_address} marked as read.")
    else:
        print("Invalid email index number.")
    

# END OF READ EMAILS FUNCTION #

#-------------------------------------------------------------------------------------------------------------------#

# VIEW UNREAD EMAILS FUNCTION #
def view_unread_emails():
    # Create a function that displays all unread Email object subject lines along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    
    print("Unread emails: \n\n")
    for i, email in enumerate(inbox):
        if email.has_been_read == False:
            print(f"{i}, {email.subject_line}\n")

# END OF VIEW UNREAD EMAILS FUNCTION #

#-------------------------------------------------------------------------------------------------------------------#

# --- LISTS --- #
# Initialise an empty list outside the class to store the email objects.
inbox = []
    
#-------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------#


# --- MAIN Email Program --- #
# Call the function to populate the inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
# Display the menu options for each iteration of the loop.

while True:
    print("Select an option (type the number only): ")
    print("1 - Read an email\n2 - View unread emails\n3 - Quit application")
    option = int(input("\nOption: "))
    
    if (option == 1):
        #read email
        print("\nWhich email would you like to read? Enter the number only.")
        list_emails()
        i = int(input("\nEmail number: "))
        read_email(i)
        
    elif (option == 2):
        #view unread emails
        view_unread_emails()
        
    elif (option == 3):
        print("\nQuitting application.")
        break
        #quit
    else:
        print("Invalid option.")




print("\n--------------------------------------------------------\n")



