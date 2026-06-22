# we can make our own custom libraries to bring in code from; let's say you find yourself repeatedly using the same codes over and over

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")




if __name__ == "__main__": # this line is inputted so that main isn't recalled from the program, otherwise if you just wanted to input hello, then it would read it from hello all the way to the bottom of main, which recalls the entire program, regurgitating everything
    main() # this will now get ignored when importing as a library as we are not recalling main
