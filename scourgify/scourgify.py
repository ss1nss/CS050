import csv
import sys


def main():

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV File")
        if not sys.argv[2].endswith(".csv"):
            sys.exit("Not a CSV File")
        else:
            scourgify(input_file, output_file)


def scourgify(input, output):
    try:
        with open(input) as input:
            reader = csv.DictReader(input)
            with open(output, "w") as output:
                writer = csv.DictWriter(output, fieldnames = ["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(",")
                    house = row["house"]
                    writer.writerow({"first": first.strip(), "last": last.strip(), "house": house.strip()})
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")


if __name__ == "__main__":
    main()

