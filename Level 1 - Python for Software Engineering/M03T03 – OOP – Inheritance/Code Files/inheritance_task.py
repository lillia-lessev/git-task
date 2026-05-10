"""
----------------------------------------------

Lillia Lessev

OOP - Inheritance

----------------------------------------------

"""


class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # Method to show Head Office location
    def head_office_location(self):
        print("The Head Office is in Cape Town.")

class OOPCourse(Course):
    # Constructor Method
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    # Method to print trainer details
    def trainer_details(self):
        print(f"The course is about {self.description} and the trainer is {self.trainer}")

    # Method to show course ID
    def show_course_id(self):
        print("Course ID: #12345")


print("\n--------------------------------------------------------\n")

# Example usage:
# Create an instance of the Course class
course_1 = OOPCourse()

# Call the contact_details method to display contact information
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()

print("\n--------------------------------------------------------\n")