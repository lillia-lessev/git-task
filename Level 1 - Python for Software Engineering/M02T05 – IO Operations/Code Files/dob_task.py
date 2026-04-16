"""
----------------------------------------------

Lillia Lessev

IO Operations


----------------------------------------------

"""

print("\n--------------------------------------------------------\n")

names = []
bdays = []
line_parts = []

with open("Level 1 - Python for Software Engineering\M02T05 – IO Operations\Code Files\Input\Task file\DOB.txt", "r") as file:
    for line in file:
        line_parts = line.strip().split()       # removes leading and trailing whitespace, spaces, tabs and '\n' from each line
                                                # also splits string / line by spaces / whitespaces
                                                # strip() removes whitespace AND \n while .strip(" ") does not
                                                # .split() with no argument splits on any whitespace and collapses multiple spaces/tabs into one separator.
        if len(line_parts) >= 3:
            names.append(" ".join(line_parts[:2]))
            bdays.append(" ".join(line_parts[2:]))
        

names_length = len(names)
print("\nNAME:\n")
for i in range(0, names_length):
    print(names[i])

bdays_length = len(bdays)
print("\nBIRTHDATE:\n")
for i in range(0, bdays_length):
    print(bdays[i])
    

print("\n--------------------------------------------------------\n")
