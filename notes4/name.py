# command-line arguments are features in all languages that allows you to provide input not just when prompted inside of a program in a function like input()
# let's make an argument using the sys module, whichb contains a whole list of coimmand line codes related to systems

#import sys # sys.argv = argument vector, list of all words that the user typed in in their prompt before they hit enter; meaning, first word is the first element, second word second el, etc
# importing sys gives access to sys.argv

# instead of writing hello world program that looks for the return value of the input, we can go ahead expect the user to tell them their name when the program is run
#print("hello, my name is", sys.argv[1]) # sys.argv[0] is the name of the program

# now you can run the program as python name.py Paul, program now runs without asking for input and directly gives the print with name
# only really works if the user inputs the "list" when running the program
# so instead we could do a try function to reprompt a name

import sys

#try:
#    print("hello, my name is", sys.argv[1])
#except IndexError:
#    print("Too few arguments") # this does give the user back a response instead of the cryptic line breaks, but it's still a bit reactive, we can be more defensive

# using len we can make it so that we restrict the word inputted from the user
# if you type no name, too few arguments
# if you type like first and last name, too many arguments
# python name.py Paul will get printed
#if len(sys.argv) < 2:
#    print("Too few arguments")
#elif len(sys.argv) > 2:
#    print("Too many arguments")
#else:
#    print("hello, my name is", sys.argv[1])

# let's make the code appear nicer, logically it still makes sense, but we want to keep the error checks separate from the correct flow

# this checks for errors
#if len(sys.argv) < 2:
#    sys.exit("Too few arguments") # sys.exit will exit out of the program when run and conditions are met, and not go through the rest of teh script
#elif len(sys.argv) > 2:
#    sys.exit("Too many arguments")

# Print name tags
#print("hello, my name is", sys.argv[1])

# so now let's say we want to have an argument made so it can take any number of names
# we need to remove the argument for multiple arguments, to allow for first last etc
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]: # for whatever arguments are listed inside of the argv/ program when run itself, print the names; [1:-1] removes the last input for -1
    print("hello, my name is", arg) # this will print out all name tags, including 0 for the program name; we need to "slice" the list
# slices = subset of a list; [1:] slices the list to print everything from 1 to ~numbers
