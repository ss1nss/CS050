# this is how to now read the file you made

#with open("names.txt", "r") as file:
#    lines = file.readlines()

#for line in lines:
#    print("hello,", line.strip()) # print always adds a line at the end, the current text file already contains line breaks, so print is in fact adding double breaks; what you can do is strip from the variable and let porint handle the line break
## the 2 functions added creates 2x works becuase you are reading all the lines to just print each item i nthe txt file

#with open("names.txt", "r") as file:
#    for line in file: # for line in file pretty much handles like reading
#        print("hello,", line.rstrip())

## you do get each line printed out, but what if you wanted to sort the names of the file; of course you can manually change it within the txt file itself, but how can we sort feasibly?
## if you only cared the file is sorted, we can make a compact program per below

#with open("names.txt") as file:
#    for line in sorted(file):
#        names.append(line.rstrip())

# otherwise, we can sort by whatever is within the file and adding it to a list, this way we can not only sort, but uppercase, lowercase, etc.

names = [] # back tracking, we are adding a names list

with open("names.txt") as file: # same start, we are opening the file and giving it the variable called "file"
    for line in file:
        names.append(line.rstrip()) # we are appending the list of names within the "line" in the file called "file"; stripping the break


for name in sorted(names, reverse=True): # we added the name to names list and then outside of the strip, we print out as "sorted()" for the list made from memory
                            # reverse=True, reverses the order from z - a; sorted is part of the python library, a lot of syntax can be added as needed
    print(f"hello, {name}") # now you print out the individual "name"


