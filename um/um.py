import re
import sys


def main():
    if len(sys.argv) == 1:
        text = input("Text: ")
    elif len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        sys.exit("Invalid Input")

    print(count(text))

def count(s):
    match = re.findall(r"\bum\b", s, re.IGNORECASE) # \b for word character boundary at the beginning and end, ensuring only the standalone um is/are counted regardless of non-word characters
    return len(match)



if __name__ == "__main__":
    main()
