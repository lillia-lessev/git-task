"""
----------------------------------------------

Lillia Lessev

Programming With Built-In Functions

----------------------------------------------

"""
import random



print("\n--------------------------------------------------------\n")

joke_1 = "What did one hat say to the other?\nYou wait here. I’ll go on a head."
joke_2 = "What do you call a magic dog?\nA labracadabrador."
joke_3 = "What’s orange and sounds like a carrot?\nA parrot."
joke_4 = "What did the pirate say when he turned 80?\nAye matey."
joke_5 = "Why do Black Labs hate the rain?\nThey don't want to step in a poodle!"
joke_6 = "Why dont Black Labs bark at their feet?\nBecause its not polite to talk back to your Paw!"
joke_7 = "What do cows do on date night?\nGo to the moo-vies."
joke_8 = "What do cows say when they hear a bad joke?\n“I am not amoosed.”"
joke_9 = "Why do French people eat snails?\nThey don’t like fast food."
joke_10 = "How many tickles does it take to make an octopus laugh?\nTen-tickles."

joke_list = [joke_1, joke_2, joke_3, joke_3, joke_4, joke_5, joke_6, joke_7, joke_8, joke_9, joke_10]

rand_joke = random.choice(joke_list)
print(rand_joke)

print("\n--------------------------------------------------------\n")
