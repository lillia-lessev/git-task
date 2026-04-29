"""
----------------------------------------------

Lillia Lessev

STACK TRACE

----------------------------------------------

"""


# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) # changed k to key

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", # changed '' to ""
                         "maggie": "(Pacifier Suck)"
                         }

print()
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])
print()

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

