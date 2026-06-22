# making a math equation to have x and z as an integer and y as arithmetic symbols; x will cover the numbers and y will cover the symbols, z will be the result


expression = input("Expression: ")
x, y, z = expression.split(" ")
if y == "+":
    print(f"{int(x) + int(z):.1f}")
elif y == "-":
    print(f"{int(x) - int(z):.1f}")
elif y == "*":
    print(f"{int(x) * int(z):.1f}")
elif y == "/":
    print(f"{int(x) / int(z):.1f}") #assuming 0 will not be used to divide x number


