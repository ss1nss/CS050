# making a very basic calculator
# setting the variables as an input
# x = input("what is x? ")
# y = input("what is y? ")

# creating the basic formula for addition in this case, making the variables as integers; if they are not integers the strings will be cascaded
# int = integer (-2, -1, 0, 1, 2, ...etc)
# z = int(x) + int(y)

# print out the equation
# print(z)

# cleaner formula if the specific task is the above
# x = int(input("what is x? "))
# y = int(input("what is y? "))

# print(x + y)

# but let's say we want to add in decimals, then we need floating numbers (float)
x = float(input("what is x? "))
y = float(input("what is y? "))

# if the result is to be rounded regardless of the input, input round
# print(round(x + y))

# let's go back to the original equation with z
# so that we can get data for accounting numbers, or rather, us formats
z = round(x + y)

# inputting the f string allows for syntax to tell the numbers to be formatted with the comma
print(f"{z:,}")
