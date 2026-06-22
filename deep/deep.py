# making a yes or no answer for different 42's inputted for the input asked
n = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lstrip().lower().rstrip()
match n:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")
