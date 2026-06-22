# making a string for camel input to result in snake output
string = input("camelCase: ")
print("snake_case: ", end="")

# for any _ in my original camel input, if there is a upper case, print "_" before the capital and then make it lower; no line breaks, syntax in 1 line
for capitals in string:
    if capitals.isupper():
        print("_" + capitals.lower(), end="")
    else:
        print(capitals, end="")
print("") #adding line break for the start of the next code input

#for regex
#import re
#def snake(a):
#    return re.sub(r"([A-Z])", r"_\1", a).lower()
