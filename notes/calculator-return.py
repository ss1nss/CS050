# let's say you want to write code for what ahs already been defined, but you want to keep adding in mroe definitions as you go
# well, you will have to encase everything in a overall def function, kind of like html's <main></main>, that way when you define a code, it will read from bottom to top as well as top to bottom for variables

def main():
    x = float(input("What's X? ")) #(or int)
    print("x squared is", square(x))

# I am later working backwards by adding in the variable and how square() should be defined per below
def square(n):
# ** mean power of 2, returns the value of n squared; can change accordingly power of 3 **3, etc
    return n**2




# closing of the encapsulating code
main()
