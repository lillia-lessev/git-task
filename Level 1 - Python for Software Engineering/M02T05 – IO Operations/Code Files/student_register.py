"""
----------------------------------------------

Lillia Lessev

IO Operations


----------------------------------------------

"""

print("\n--------------------------------------------------------\n")

# VARIABLES
num_stu = 0
id = 0
stu_id = []
dotted_line = "\t......................\n"
stu_lines = []

# ENTERING NO. OF STUDENTS
print("REGISTER STUDENTS FOR EXAM VENUE\n")
num_stu = int(input("How many students are being registered? Number: "))

# GETTING STUDENT IDs AND STORING THEM
for i in range(0, num_stu):
    id = input(f"Student {i+1} ID: ")
    stu_id.append(id) # collect info as list and then only write the list
    stu_lines.append(stu_id[i] + dotted_line)
    #file.write(stu_lines + "\n")
    
#print(stu_lines)

# WRITING DATA TO TEXT FILE
try:
    
    
    with open("reg_form.txt", "w+", encoding="utf-8") as file:
        file.write("STUDENT REGISTERED FOR EXAM VENUE:\n\n")
        file.write("".join(stu_lines)) # Can't just say file.write(stu_lines) because .write(str) must be string not list. .join() converts it to a string
        #file.write(str(stu_lines)) # Can't do this because then it's just going to print the list on one line like this e.g.  [blah blah\n...\n\]    
        
except FileNotFoundError:
    print("File does not exist.")

print("\n--------------------------------------------------------\n")


'''
ORIGINAL CODE:

num_stu = 0
id = 0
stu_id = []
dotted_line = "\t......................"
stu_line = ""

# learnt about pathlib etc from Python Software Foundation (n.d.). See full reference at the end of the project.


# from pathlib import Path #importing the main class

# base = Path(__file__).resolve().parent # getting parent directory
# filepath = base / "reg_form.txt"



print("REGISTER STUDENTS FOR EXAM VENUE\n")
num_stu = int(input("How many students are being registered? Number: "))
# ctr + / will comment out selected code 


print("\nENTERING STUDENT IDs\n")




try:
    
    
    with open("reg_form.txt", "w+", encoding="utf-8") as file:
    #with filepath.open("w+", encoding="utf-8") as file: # Python Software Foundation (n.d.). See full reference at the end of the project.
        print("\nENTERING STUDENT IDs\n")
        file.write("STUDENT REGISTERED FOR EXAM VENUE:\n\n")
        for i in range(0, num_stu):
            id = input(f"Student {i+1} ID: ")
            stu_id.append(id) # collect info as list and then only write the list
            stu_line = stu_id[i] + dotted_line
            file.write(stu_line + "\n")
            # shift + tab tabs backwards
            
            
            
            
            # create string as a string and then write it to the file
            
            # Get input in its own for loop
            
            # write to the file in its own separate code block
            # remember to always include encoding e.g. utf-8
            
            # # Writing data to file
            # with open("reg_form.txt", "w+", encoding="utf-8") as file:
            #     file.write("\n".join(data_list))
            
            
except FileNotFoundError:
    print("File does not exist.")


'''





''' 
move to folder you're working in 

COMMANDS:

dir  --> shows directory?

e.g. cd folder_1

cd .. --> one folder back / parent directory
cd . --> current directory

This method might struggle if folders have spaces in their names

File > Open Folder > (Open specific folder you want)




-----------





'''



""" 
-------------------------------------------------------------------------
REFERENCES: (APA 7 Style)
-------------------------------------------------------------------------

Python Software Foundation. (n.d.). pathlib — Object-oriented filesystem paths — Python 3.9.4 documentation. Docs.python.org. https://docs.python.org/3/library/pathlib.html 


-------------------------------------------------------------------------

"""