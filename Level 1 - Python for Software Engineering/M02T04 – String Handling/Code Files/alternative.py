"""
----------------------------------------------

Lillia Lessev

String Handling

----------------------------------------------

"""
print("\n---------------------------------------\n")


message = str(input("Please input a message: "))
message = message.lower()
message_length = int(len(message))
message_characters = []
new_message = ""

# ALTERNATING LETTERS
print("\nALTERNATING LETTERS:\n")
for i in range(0, message_length):
    if ((i % 2) != 0):
        character = message[i].upper()
        new_message += character
    elif ((i % 2) == 0):
        character = message[i].lower()
        new_message += character
print(new_message)


# ALTERNATING WORDS
new_message = ""
print("\n\nALTERNATING WORDS:\n")
words = message.split(" ")
words_length = len(words)
current_word = ""
for i in range(0, words_length):
    if ((i % 2) != 0):
        current_word = words[i].upper()
        words[i] = words[i].replace(words[i], current_word)
        #new_message = new_message.join([words[i].upper(), " "])
        new_message = (words[i].upper()).join([new_message, " "])

    elif ((i % 2) == 0):
        current_word = words[i].lower()
        words[i] = words[i].replace(words[i], current_word)
        #new_message = new_message.join([words[i].lower(), " "])
        new_message = (words[i].lower()).join([new_message, " "])


        
print(new_message)
print("\n---------------------------------------\n")

