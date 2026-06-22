# libray is just written codes you can use in a code you setup
# modules are a library with function(s) built into it; let's say you find yourself inputting the same lines of code each time in new projects, simply link the code to the module
# modules allows for quicker accessibility, not having to copy paste the same line of code over and over
# example in python, there is a file called random.py that pretty much is coded for rng
# you can link to the specific random module for random in python's website, instead of having to write a code that simulates randomness

#import # allows you to "import" a the contents of a python module
#random.choice(seq) # this is the random module for choice, seq stands for sequence of a list; could be numbers or strings

#let's make a program for fliping a coin, 50/50 heads or tails

#import random # importing random module

#coin = random.choice(["heads", "tails"]) # I'm using the random script/ module and setting it as choice. within the string I setup a list for heads or tails
# random.choice simply returns an item in the list with equal probability
#print(coin)

# alternatively, instead of importing random, we can state from random import choice

from random import choice # this allows you to say that from that random module you are specifying the import on choice; instead of contantly writing random.choice
#allows you to set the scope, ex, what if the random moduule grabbed from generate, then generate grabbed from random? creates a conflict unless we specify
#either way works, and not necessarily better than the other, it depends on the scope of your code

coin = choice(["heads", "tails"])
print(coin)
