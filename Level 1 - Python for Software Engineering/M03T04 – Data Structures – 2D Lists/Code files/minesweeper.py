"""
----------------------------------------------

Lillia Lessev

2D lists

----------------------------------------------

"""

print("\n--------------------------------------------------------\n")

#   '#' are mines

grid = [["-", "-", "-", "#", "#"], 
        ["-", "#", "-", "-", "-"], 
        ["-", "-", "#", "-", "-"], 
        ["-", "#", "#", "-", "-"], 
        ["-", "-", "-", "-", "-"]]

'''
KEY:
ER = Edge Row
EC = Edge Column
MR = Middle Rows
MC = Middle Coolumns

'''


def check_row(row_number):
    if (row_number != 0) and (row_number != 4):
        #print(f"Row {row_number}: Not top or bottom row.") 
        row_state = "MR"
        return row_state    
    elif (row_number == 0):
        #print(f"Row: {row_number}: Edge row.")
        row_state = "ER0"
        return row_state 
    elif (row_number == 4):
        #print(f"Row: {row_number}: Edge row.")
        row_state = "ER4"
        return row_state 

def check_column(column_number):
        if (column_number != 0) and (column_number != 4):
            #print(f"\tColumn {column_number}: Not an edge Column.")
            column_state = "MC"
            return column_state
        elif (column_number == 0) :
            #print(f"\tColumn {column_number}: Edge Column.")
            column_state = "EC0"
            return column_state
        elif (column_number == 4):
            #print(f"\tColumn {column_number}: Edge Column.")
            column_state = "EC4"
            return column_state


def check_empty(grid, row_number, column_number, my_grid):
        
        if (grid[row_number][column_number] == "-"):
            #print("\t\tEmpty") 
            my_grid[row_number][column_number] = my_grid[row_number][column_number]
            
        elif(grid[row_number][column_number] == "#"):
            #print("\t\tMine")
            my_grid[row_number][column_number] = "#"

def count_mines(value):
    if (value != "#"):
        value += 1
    elif (value == "#"):
        pass
    return value      

def check_mines(my_grid, row_number, column_number):
    
    value = my_grid[row_number][column_number]
    
    row_state = check_row(row_number)
    column_state = check_column(column_number)

    if (value == "#"):
        if (row_state == "ER0") and (column_state == "EC0"):
            after_value = my_grid[row_number][column_number + 1]
            if (after_value != "#"):
                after_value = count_mines(after_value)
                my_grid[row_number][column_number + 1] = after_value
            
            bottom_value = my_grid[row_number + 1][column_number]
            if (bottom_value != "#"):
                bottom_value = count_mines(bottom_value)
                my_grid[row_number + 1][column_number] = bottom_value
            
            bottom_R_diag_value = my_grid[row_number + 1][column_number + 1]
            if (bottom_R_diag_value != "#"):
                bottom_R_diag_value= count_mines(bottom_R_diag_value)
                my_grid[row_number + 1][column_number + 1] = bottom_R_diag_value
        
        elif (row_state == "ER0") and (column_state == "EC4"):
            
            before_value = my_grid[row_number][column_number - 1]
            if (before_value != "#"):
                before_value = count_mines(before_value)
                my_grid[row_number][column_number - 1] = before_value
                
            bottom_value = my_grid[row_number + 1][column_number]
            if (bottom_value != "#"):
                bottom_value = count_mines(bottom_value)
                my_grid[row_number + 1][column_number] = bottom_value
            
            bottom_L_diag_value = my_grid[row_number + 1][column_number - 1]
            if (bottom_L_diag_value != "#"):
                bottom_L_diag_value = count_mines(bottom_L_diag_value) 
                my_grid[row_number + 1][column_number - 1] = bottom_L_diag_value 
        
        elif (row_state == "ER0") and (column_state == "MC"):
            after_value = my_grid[row_number][column_number + 1]
            if (after_value != "#"):
                after_value = count_mines(after_value)
                my_grid[row_number][column_number + 1] = after_value
            
            before_value = my_grid[row_number][column_number - 1]
            if (before_value != "#"):
                before_value = count_mines(before_value)
                my_grid[row_number][column_number - 1] = before_value
            
            bottom_value = my_grid[row_number + 1][column_number]
            if (bottom_value != "#"):
                bottom_value = count_mines(bottom_value)
                my_grid[row_number + 1][column_number] = bottom_value
            
            bottom_L_diag_value = my_grid[row_number + 1][column_number - 1]
            if (bottom_L_diag_value != "#"):
                bottom_L_diag_value = count_mines(bottom_L_diag_value) 
                my_grid[row_number + 1][column_number - 1] = bottom_L_diag_value 
            
            bottom_R_diag_value = my_grid[row_number + 1][column_number + 1]
            if (bottom_R_diag_value != "#"):
                bottom_R_diag_value= count_mines(bottom_R_diag_value)
                my_grid[row_number + 1][column_number + 1] = bottom_R_diag_value
        
        elif (row_state == "MR") and (column_state == "MC"):
            after_value = my_grid[row_number][column_number + 1]
            if (after_value != "#"):
                after_value = count_mines(after_value)
                my_grid[row_number][column_number + 1] = after_value
                
            before_value = my_grid[row_number][column_number - 1]
            if (before_value != "#"):
                before_value = count_mines(before_value)
                my_grid[row_number][column_number - 1] = before_value
            
            bottom_value = my_grid[row_number + 1][column_number]
            if (bottom_value != "#"):
                bottom_value = count_mines(bottom_value)
                my_grid[row_number + 1][column_number] = bottom_value
            
            bottom_L_diag_value = my_grid[row_number + 1][column_number - 1]
            if (bottom_L_diag_value != "#"):
                bottom_L_diag_value = count_mines(bottom_L_diag_value) 
                my_grid[row_number + 1][column_number - 1] = bottom_L_diag_value 
            
            bottom_R_diag_value = my_grid[row_number + 1][column_number + 1]
            if (bottom_R_diag_value != "#"):
                bottom_R_diag_value= count_mines(bottom_R_diag_value)
                my_grid[row_number + 1][column_number + 1] = bottom_R_diag_value
            
            top_value = my_grid[row_number - 1][column_number]
            if (top_value != "#"):
                top_value = count_mines(top_value)
                my_grid[row_number - 1][column_number] = top_value
            
            top_L_diag_value = my_grid[row_number - 1][column_number - 1]
            if (top_L_diag_value != "#"):
                top_L_diag_value = count_mines(top_L_diag_value)
                my_grid[row_number - 1][column_number - 1] = top_L_diag_value
            
            top_R_diag_value = my_grid[row_number - 1][column_number + 1]
            if (top_R_diag_value != "#"):
                top_R_diag_value = count_mines(top_R_diag_value)
                my_grid[row_number - 1][column_number + 1] = top_R_diag_value
        
        elif (row_state == "MR") and (column_state == "EC0"):
            after_value = my_grid[row_number][column_number + 1]
            if (after_value != "#"):
                after_value = count_mines(after_value)
                my_grid[row_number][column_number + 1] = after_value
            
            bottom_value = my_grid[row_number + 1][column_number]
            if (bottom_value != "#"):
                bottom_value = count_mines(bottom_value)
                my_grid[row_number + 1][column_number] = bottom_value
            
            bottom_R_diag_value = my_grid[row_number + 1][column_number + 1]
            if (bottom_R_diag_value != "#"):
                bottom_R_diag_value= count_mines(bottom_R_diag_value)
                my_grid[row_number + 1][column_number + 1] = bottom_R_diag_value
            
            top_value = my_grid[row_number - 1][column_number]
            if (top_value != "#"):
                top_value = count_mines(top_value)
                my_grid[row_number - 1][column_number] = top_value
            
            top_R_diag_value = my_grid[row_number - 1][column_number + 1] 
            if (top_R_diag_value != "#"):
                top_R_diag_value = count_mines(top_R_diag_value)
                my_grid[row_number - 1][column_number + 1] = top_R_diag_value
        
        elif (row_state == "MR") and (column_state == "EC4"):
            before_value = my_grid[row_number][column_number - 1]
            if (before_value != "#"):
                before_value = count_mines(before_value)
                my_grid[row_number][column_number - 1] = before_value
            my_grid[row_number][column_number - 1] = before_value
            
            bottom_value = my_grid[row_number + 1][column_number]
            if (bottom_value != "#"):
                bottom_value = count_mines(bottom_value)
                my_grid[row_number + 1][column_number] = bottom_value
            
            bottom_L_diag_value = my_grid[row_number + 1][column_number - 1]
            if (bottom_L_diag_value != "#"):
                bottom_L_diag_value = count_mines(bottom_L_diag_value) 
                my_grid[row_number + 1][column_number - 1] = bottom_L_diag_value 
            
            top_value = my_grid[row_number - 1][column_number]
            if (top_value != "#"):
                top_value = count_mines(top_value)
                my_grid[row_number - 1][column_number] = top_value
            
            top_L_diag_value = my_grid[row_number - 1][column_number - 1]
            if (top_L_diag_value != "#"):
                top_L_diag_value = count_mines(top_L_diag_value)
                my_grid[row_number - 1][column_number - 1] = top_L_diag_value
    else:
        if (isinstance(value, int)):
            pass
    
        
my_grid = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]

row_number = 0

index = 0
print("----BEFORE----\n")
for row in grid:
    print(grid[index])
    index +=1

for row in grid:
    
    check_row(row_number)
    column_number = 0
    
    for column in row:
        
        check_column(column_number)
        check_empty(grid, row_number, column_number, my_grid)
        column_number += 1
        
    row_number +=1


row_number = 0
for my_row in my_grid:
    column_number = 0

    for my_column in my_row:
        check_mines(my_grid, row_number, column_number)
        column_number += 1
    
    row_number += 1   

index = 0
print("\n----AFTER----\n")
for my_rows in my_grid:
    print(my_grid[index])
    index +=1
print("\n--------------------------------------------------------\n")