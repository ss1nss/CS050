import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            print(create_table(sys.argv[1]))

def create_table(python_file):
    try:
        with open(python_file) as csvfile:
            reader = csv.reader(csvfile)
            table = list(reader)
            tabulated = tabulate(table, headers="firstrow", tablefmt="grid")
            return tabulated
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
