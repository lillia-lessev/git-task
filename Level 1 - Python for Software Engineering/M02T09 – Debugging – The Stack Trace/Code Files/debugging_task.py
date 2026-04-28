"""
----------------------------------------------

Lillia Lessev

STACK TRACE

----------------------------------------------

"""


# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    # for keys in dictionary:                       # changed keys to dictionary and changed key to keys
    #     print(dictionary[keys])                   # changed [k] to [keys]
    #commented out for loop and wrote print statement below instead
    print(dictionary[keys])

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!",          #changed '' to "" 
                         "maggie": "(Pacifier Suck)"
                         }


#print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer') 
#replaced above commented-out line with lines below

print_values_of(simpson_catch_phrases, "lisa")
print_values_of(simpson_catch_phrases, "homer")
print_values_of(simpson_catch_phrases, "bart")


'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

