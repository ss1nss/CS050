# we can make a loop with For as well
# we need a list as well to compare for to
# list is just a list of things, pinning multiple variables in teh same place

# for everything in the list, print meow
#for i in [0, 1, 2]:
#    print("meow")

# the list is good, because it accomplishes the loop we want. But what about extreme cases, like 1 million or something?
# range allows you to set the upper limit, so change the number to whatever you need instead of doing 0, 1, 2, 3, ...
#for i in range(3):
#    print("meow")

# when you make a code/ function without a named variable, leave it as _ as it is pythonic
#for _ in range(3):
#    print("meow")

# you can also multiply your prints
# \n allows the meows to break into next lines, end="" eliminated the final line break after the last meow
print("meow\n" * 3, end="")
