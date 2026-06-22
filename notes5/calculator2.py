# in python, we want to be more proactive in running and testing our programs
#

def main():
    x = input("What's x? ") # if you remove int, and input a str, then you will get TypeError
    print("x squared is", square(x))

def square(n):
    return n + n # going to give the wrong arithmetic symbol to try the test function

if __name__ == "__main__": # we're doing this proactively so that when you are importing functions from a library, main is not automatically called back
    main() # now main isn't always called, only for this specific data set, can now safely import libraries

# code is methodically correct, when running; but what about infinite numbers, negatives, 0s, etc; how do we proactively test the code before submitting it?
