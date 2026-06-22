# I've been writing "hello," too much, is there a way where I can substitue it as a function, so if I say hello(), it'll automatically populate "hello," ?

# I define hello() as a function, in the next line, indent whatever you want so that whenever you type the hello() function, whatever is indented pops out
#def hello():
#    print("hello")

# you can add another parameter to define in the parentheses such as to = world, that way you can print the mention of to as world
def hello(to="world"):
    print("hello,", to)

# hello() is now a function, you can define in the earlier "creation" of the function 1\n for line break or sep for spaces
hello()
name = input("What's your name? ")
hello(name)
