# match

# for instance, we are trying to figure our based on name, which house each person belongs under
name = input("What's your name? ")

#if name == "Harry":
#    print("Gryffindor")
#elif name == "Hermione":
#    print("Gryffindor")
#elif name == "Ron":
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who?")

# we can condense this code even more by adding the or line into the if statement
#if name == "Harry" or name == "Hermione" or name == "Ron":
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who?")

# match allows you to enter cases where if person is listed, will return the print
match name:
#    case "Harry":
#        print("Gryffindor")
#    case "Hermnione":
#        print("Gryffindor")
#    case "Ron":
#        print("Gryffindor")

# instead of writing 3 people part of the same print in 3 separate lines, again, you can put them all in one syntax by using shift + \ (|)
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
# we can add a catch all for the other names inputted
    case _:
        print("Who?")
