# parity = even or odd
# + = addition
# - = subtraction
# * = multiplication
# / = division
# % = division, but for the remainder remaining so 1 % 3 == 1 because reaminder is 1

#x = int(input("What's X? "))

#in this example, we are stating if x divided by 2 with remainder equaling 0, the nuumber is cleanly "evening" itself out
#if x % 2 == 0:
#    print("Even")
#else:
#    print("Odd")

# Let's make this in to a formula instead
def main():
    x = int(input("What's X? "))
    # making a formula which will be defined later
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# we're making this into a formula to return boolean values; bools can only be true/ false
# I now have a function that has is even for finding out if something is even or odd
def is_even(n):
#    if n % 2 == 0:
#        return True
#    else:
#        return False

# there is another way of writing out the definition instead of 2 returns
# this way, we are getting the boolean in one argument
#    return True if n % 2 == 0 else False

# so we can actually just enter the answer, there is no need for true or false in this case because the original syntax covers that true/ false
    return n % 2 == 0

main()
