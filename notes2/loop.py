# let's figure out how to get a number from a user, example, user needs to give positive value

#n = int(input(""What's n? "))
#if n < 0:
    #n = int(input("What's n? ")) # this will forever go on a loop because you are making sure only a positive input is given, until the user concedes. program wil never be completed

# the above scenario is not realistically possible for the programmer, to check for these instance we can use while; this can produce an infinite loop
#while True:
#    n = int(input("What's n? "))
#    if n < 0:
#        continue #continue to stay in this loop if false
#    else:
#        break #if true, break the loop

#for _ in range(n):
#    print("meow")

# let's try making a main function for meowing multiple times
def main():
    number = get_number()
    meow(3)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n # you can break here as well, stopping the loop; but you need to return n at the end of the function

def meow(n)
    for _ in range(n):
        print("meow")





(main)
