# in python, or really in any coding applications, symbols are used for conditions
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == equal to
# != does not equal

x = int(input("What's x? "))
y = int(input("What's y? "))

# made an if statement to make a boolean expression of yes or no, true or false, etc of two choices
# program below is very basic, we are making several if statements and whatever we "input" for x and y, will always need to go through each of those questions
# add el to if to stop asking the question if 1 < 2, that's true, it will not go through the rest of the statements
# without el, the same 1 < 2 will be asked to each of the if statements before the code stops, this will create a lotta lag; especially noticeable if we had a huge block of code
# example for boolean: if x < y = true, then print will be the result; if false, it will move into the next argument
if x < y:
    print("x is less than y")
# example for boolean: if x > y = true, then print will be the result; if false, it will move into the next argument
# el keeps the question going if the prior question was false, otherwise the code stops
elif x > y:
    print("x is greater than y")
# example for boolean: if x == y = true, then print will be the result; finally the code stops
# el keeps the question going if the prior question was false, otherwise the code stops
#elif x == y:
#    print("x is equal to y")

# Well actually, you don't even need that last argument, if both statements are false, then the last has to be true
# so instead, write else
else:
    print("x is greater than y")
