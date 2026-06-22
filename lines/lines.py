import sys

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
        else:
            print(count_code(sys.argv[1]))

def count_code(python_file):
    try:
        lines = 0
        with open(python_file) as file: # default "r"
            for row in file:
                if row.strip() and not row.strip().startswith("#"): # if something's in a row in the python file but not "nothing" and not if the row starts with #; lines count goes up
                    lines += 1
        return lines
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
