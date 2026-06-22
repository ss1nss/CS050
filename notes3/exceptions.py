# Let's say we wanted to be proactive in reporting error found
# For that, we can add in *Try as the beginning string function and *Except
#try:
#    x = int(input("What's X? "))
#except ValueError: # since we are stating the input for x as an integer, letters or even decimals cannot be inputted. In which case we are stating ValueError for non-number inputs
#    print("x is not an integer")
#else: # argument flows through normally once the exception check clears
#    print(f"x is {x}")

#while True: # let's reprompt them for a response instead of saying x is not "" and ending the argument
#    try:
#        x = int(input("What's X? "))
        #break # can also state break here instead
#    except ValueError:
#        print("x is not an integer")
#    else:
#        break


#print(f"x is {x}")

def main():
    x = get_int("What's x? ") #making a function called get_int
    print(f"x is {x}")

#def get_int():
#    while True:
#        try:
#            x = int(input("What's X? "))
#        except ValueError:
#            print("x is not an integer")
#        else:
#            break
#    return x

#def get_int():
#    while True:
#        try:
#            x = int(input("What's X? ")) #you don't need to give a variable here, can instead say return int(input("What's X? "))
#            return x #you can state it here
#        except ValueError:
#            print("x is not an integer")
##        else:
##            return x #you can just say return the value, not only does it break the argument, but also gives you the result; way cleaner

#pass
def get_int(prompt): #I added what's x in the function get int; substituing it with prompt
    while True:
        try:
            return int(input(prompt)) #now you can say prompt here from the get int variable, does not need to be named prompt, can be named other things in both areas x, y z, 01, etc
        except ValueError:
            pass #will reloop the error, passing the error through the argument, just no statement given











main()
