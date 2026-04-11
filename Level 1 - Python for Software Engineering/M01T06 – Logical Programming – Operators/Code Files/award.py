"""
----------------------------------------------

Lillia Lessev
    
Logical Programming - Operators

----------------------------------------------

"""



print("\n--------------------------------------------\n")

minutes = 0
seconds = 0
sub_minutes = 0
total_minutes = -1

award1 = "Provincial Colours"
award2 = "Provincial Half Colours"
award3 = "Provincial Scroll"
award4 = "No award"

print(f'''\nCongrats on completing your triathlon!\nPlease enter your time (in WHOLE numbers) and press enter. Please enter your minutes first and then your seconds.\n''')


minutes = int(input("Please enter the number of minutes: "))
seconds = int(input("Please enter the number of seconds: "))

sub_minutes = float(seconds / 60)
total_minutes = minutes + sub_minutes
total_minutes = round(total_minutes, 2)


while (total_minutes < 0):
    print("\nWhoops! Please enter a positive whole number for your minutes and for your seconds and try again.")
    print(f'''\nPlease enter your time (in WHOLE numbers) and press enter. Please enter your minutes first and then your seconds.\n''')


    minutes = int(input("Please enter the number of minutes: "))
    seconds = int(input("Please enter the number of seconds: "))
    sub_minutes = float(seconds / 60)
    total_minutes = minutes + sub_minutes
    total_minutes = round(total_minutes, 2)
else:  
    if (total_minutes <= 100):
        print(f'''\nYour time was:
            \n{total_minutes} minutes
            \n({minutes} minutes, {seconds} seconds)''')
        print(f"\nAward: {award1}")
        
#   elif (total_minutes >= 101) and (total_minutes <= 105):   # --> This only works if using whole numbers ONLY, or just using the WHOLE minutes, without the decimal to account for the seconds
    elif (total_minutes >= 101) and (total_minutes < 106):    
        print(f'''\nYour time was:
            \n{total_minutes} minutes
            \n({minutes} minutes, {seconds} seconds)''')
        print(f"\nAward: {award2}")

#   elif (total_minutes >= 106) and (total_minutes <= 110): # --> This only works if using whole numbers ONLY, or just using the WHOLE minutes, without the decimal to account for the seconds
    elif (total_minutes >= 106) and (total_minutes < 111):        
        print(f'''\nYour time was:
            \n{total_minutes} minutes
            \n({minutes} minutes, {seconds} seconds)''')
        print(f"\nAward: {award3}")
        
    elif (total_minutes >= 111):
        print(f'''\nYour time was:
            \n{total_minutes} minutes
            \n({minutes} minutes, {seconds} seconds)''')
        print(f"\nAward: {award4}")
    
print("\n--------------------------------------------\n")
