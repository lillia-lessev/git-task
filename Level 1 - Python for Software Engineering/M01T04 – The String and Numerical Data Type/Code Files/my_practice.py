"""
--------------------------------------------------------------------------------------
Concatenating Strings
--------------------------------------------------------------------------------------

"""

name = "Lillia"
age = 22



print(name + " is " + str(age) + " years old.") # this is not the best option 

print("{} is {} years old.".format(name, age))
print(f"{name} is {age} years old.\n\n--------------------------------------------------------------------------------------------\n\n")


"""
--------------------------------------------------------------------------------------
Splitting Strings
--------------------------------------------------------------------------------------

"""


my_string = "Here is a list: eggs, bacon, cheese, and toast."
split_string = my_string.split(",")
data_type1 = str((type(split_string))) # casting the result to a String

print("split_string is a " + data_type1)
print(split_string)
print("--------------------------------------------------------------------------------------------\n")

tongue_twister = "She sells seashells by the seashore."
split_tongue_twister = tongue_twister.split("s")
print(split_tongue_twister)
print(str(split_tongue_twister)) # it is not necessary to cast a list to a string if you're just printing a list without concatenating it to a string.
print("--------------------------------------------------------------------------------------------\n")



"""
--------------------------------------------------------------------------------------
Stripping Strings
--------------------------------------------------------------------------------------

"""

messy_string = "&&&Let's get rid of these && ampersands && on the outside && of the string.&&&&&&&&&&&&&&&&&&&&"
stripped_string = messy_string.strip("&")
print(f"Before stripping:\n{messy_string}\n\nVS\n\nAfter stripping:\n{stripped_string}")
print("--------------------------------------------------------------------------------------------\n")


"""
--------------------------------------------------------------------------------------
Replacing Characters in Strings
--------------------------------------------------------------------------------------

"""

original_string = "Bella likes to eat plemty xomes. She's a xig xlack laxrador."
replaced_string = original_string.replace("x", "b")
replaced_string2 = replaced_string.replace("m", "n")
print(f"{original_string}\n{replaced_string}\n{replaced_string2}")
print("--------------------------------------------------------------------------------------------\n")

cypher = "xiaaf meow"
message = cypher.replace("x", "H").replace("i", "e").replace("a", "l").replace("f", "o").replace("meow", "world!")
arrow = " --> "
print(cypher, arrow, message)
print("--------------------------------------------------------------------------------------------\n")


"""
--------------------------------------------------------------------------------------
Indexing Characters in Strings
--------------------------------------------------------------------------------------

"""

""" 
1	A   0	
2	B	1
3	C	2
4	D	3	
5	E	4	
6	F	5	
7	G	6	
8	H	7	
9	I	8	
10	J	9	
11	K	10	
12	L	11	
13	M	12	
14	N	13	
15	O	14	
16	P	15	
17	Q	16	
18	R	17	
19	S	18	
20	T	19
21	U	20	
22	V	21
23	W	22	
24	X	23	
25	Y	24
26	Z   25
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
position0 = alphabet[-1]
position1 = alphabet[0]
position2 = alphabet[25]
position3 = alphabet[10:11]
position4 = alphabet[11:16]
position5 = alphabet[-5]
position6 = alphabet[:]
position7 = alphabet[::]
position8 = alphabet[:-7:3]
position9 = alphabet[2:-9:-3]
position10 = alphabet[2:-9:3]
position11 = alphabet[2:-3:-3]
position12 = alphabet[2:-3:3]
position13 = alphabet[::-1] # every character from position -1 to the position before position 0 (the 'all' position) in reverse order (every 'all' character from the 25th (-1) position to the 'all' position)
position14 = alphabet[:3]
position15 = alphabet[0:3]

length = len(alphabet)
len_data_type = type(length)
print(length, len_data_type)
print()

pos_data_type = type(position4)
pos_type2 = type(pos_data_type)
print 
print(f"The position data types are: {pos_data_type} and {pos_type2}.")
print(f"The character at position 0 is:                                                                 {position1}")
print(f"The character at position -1 is:                                                                {position0}")
print(f"The character at position 25 is:                                                                {position2}")
print(f"The characters between position 10 and 11 (position 10) are:                                    {position3}")
print(f"The characters from position 11 to 15 (11 to 16, excluding 16)are:                              {position4}")
print(f"The character at position -5 is:                                                                {position5}")
print(f"All the characters in the string are:                                                           {position6}")
print(f"All the characters in the string are:                                                           {position7}")
print(f"Every third character from the start to the 19th (-7) position is:                              {position8}")
print(f"Every (negative) third (-3) character from the 2nd position to the 17th (-9) position is:       {position9}")
print(f"Every third (3) character from the 2nd position to the 17th (-9) position is:                   {position10}")
print(f"Every (negative) third (-3) character from the 2nd position to the 23rd (-3) position is:       {position11}")
print(f"Every third (3) character from the 2nd position to the 23rd (-3) position is:                   {position12}")
print(f'''All characters in reverse order (every 'all' character from the 25th (-1) :                   {position13}\n
       Every character from position -1 (25) to the position before position 0 (the 'all' position) in reverse order
       (every 'all' character from the 25th (-1) position to the 'all' position)
       \n''')
print(f"The characters from the start ('all') to the 2nd position (til 3, excluding 3rd position) are:  {position14}")
print(f"The characters from position 0 to the 2nd position (excluding 3rd position) are:                {position15}")
print("--------------------------------------------------------------------------------------------\n")



"""
--------------------------------------------------------------------------------------
Numbers
--------------------------------------------------------------------------------------

"""

num1 = 9 / 2
num2 = int(num1)
num3 = 9 % 2 # 9/2 = 4 remainder 1, so the output is 1
print(f"9 / 2 = {num1} , therefore it is {num2} remainder {num3}")
print(float(num2))

num4 = "34.4"
num5 = 34
print(float(num4))
print(float(num5))
