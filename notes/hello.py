# = pseudocode, pretty much you can make any sort of comments after the # signs
# setting the element as name with a class of input, giving it the attribute/ text within the parentheses
# can combine the "attributes like so"
name = input("What's your name? ").strip().title()

# what if some dumb user inputs spaces into their names, well, you can "strip" the spaces before and after
# name = name.strip()

# can capitalize the first letter of the user's input
# name = name.capitalize()

# but for the user entering the first/ last name, you can use title instead; but that will probably create another problem later lol
# name = name.title()

# combine the above strings
# name = name.strip().title()

# so you can say + or , to separate the text and input; the + strings together the text/input one after another but the , adds a space between the strings text/ input
# str = string
# end="1\n" end is the end of an argument, 1\n makes it so that their is a new line, by leaving it blank "" (or entering anything besiudes 1\n) we can have the proceeding argument on the same line

# instead of below
# print("Hello,", name)

# we can have this with end *again, end can have anything inside and it will populate it along with the next string (so if I enter ABC, it will print ABCname)
# print("Hello, ", end="")
# print(name)

# we can also have
# sep = separation, depending on what you place, you can remove spaces or add something in between; so sep="ABC" will show ABCname
# print("Hello,", name, sep=" ")

# Another way is by using the f string
# input is put into squiggly brackets and f is added to the beginning of the argument
print(f"Hello, {name}")

# hmmm, how to make it so I can then answer yes or no for the age inputted
age = input("How old are you? ")
print(age, ", is that correct? ", sep="")
