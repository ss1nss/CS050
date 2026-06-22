# comparing with the or logic
x = int(input("What's x? "))
y = int(input("What's y? "))

# we make an if statement to compare 2 variables
# if statement is true print 1, if false print 2
#if x < y or x > y:
#    print("x is not equal to y ")
#else:
#    print("x is equal to y ")

# if we only care about x not equaling to y, then we can just ask that qustion, making the entire formula much simple
if x == y: # can switch to != to state not equal, but you need to flip the prints of course
    print("x is equal to y ")
else:
    print("x is not equal to y ")
