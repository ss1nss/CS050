def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello, ", to)

if __name__ == "__main__": # again, from now on, main is only called within the function made
    main()
