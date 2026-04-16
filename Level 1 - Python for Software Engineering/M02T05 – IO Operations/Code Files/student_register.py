"""
----------------------------------------------

Lillia Lessev

IO Operations


----------------------------------------------

"""

print("\n--------------------------------------------------------\n")

num_stu = 0
id = 0
stu_id = []
dotted_line = "\t......................"
stu_line = ""

# learnt about pathlib etc from Python Software Foundation (n.d.). See full reference at the end of the project.

from pathlib import Path #importing the main class

base = Path(__file__).resolve().parent # getting parent directory
filepath = base / "reg_form.txt"



print("REGISTER STUDENTS FOR EXAM VENUE\n")
num_stu = int(input("How many students are being registered? Number: "))

try:
    
    #with open("reg_form.txt", "w+") as file:
    with filepath.open("w+", encoding="utf-8") as file: # Python Software Foundation (n.d.). See full reference at the end of the project.
        print("\nENTERING STUDENT IDs\n")
        file.write("STUDENT REGISTERED FOR EXAM VENUE:\n\n")
        for i in range(0, num_stu):
            id = input(f"Student {i+1} ID: ")
            stu_id.append(id)
            stu_line = stu_id[i] + dotted_line
            file.write(stu_line + "\n")
except FileNotFoundError:
    print("File does not exist.")


print("\n--------------------------------------------------------\n")



""" 
-------------------------------------------------------------------------
REFERENCES: (APA 7 Style)
-------------------------------------------------------------------------

Python Software Foundation. (n.d.). pathlib — Object-oriented filesystem paths — Python 3.9.4 documentation. Docs.python.org. https://docs.python.org/3/library/pathlib.html 


-------------------------------------------------------------------------

"""