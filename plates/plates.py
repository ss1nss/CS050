def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0].isdigit() or len(s) == 1: #check if first character is a digit, return False if True
        return False

    for i in range(1, len(s) - 1): #range search for alhapbetical numeric number (len), and looking for the variable i from within the beginning to end
        if s[i].isdigit() and s[i + 1].isalpha() or s[i] == "0": #checks to see if after i is a letter or if i begins as a 0, returning False if True
            return False

    if s[0:6].isalnum() and len(s) <= 6: #plates can only be 6 characters long, actually, the alphanumeric search probably isn't needed...
        return True
    else:
        return False

main()
