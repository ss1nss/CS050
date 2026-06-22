# cannot use re
# validate email with installed validators

import sys
import validators

def main():

    if len(sys.argv) == 1:
        text = input("Input: ")
    elif len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        sys.exit("Invalid Input")

    print(validate(text))

def validate(s):
    email = validators.email(s)
    if email is True:
        return "Valid"
    else:
        return "Invalid"



if __name__ == "__main__":
    main()
