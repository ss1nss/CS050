import re
import sys


def main():
    if len(sys.argv) == 1:
        print(parse(input("HTML: ")))
    elif len(sys.argv) == 2:
        print(parse(sys.argv[1]))
    else:
        sys.exit("Please enter 0 or 1 arguments")

def parse(s):
    match = re.search(r'<iframe src="https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)".*?></iframe>', s)
    if match:
        text = match.group(2)
        return f"https://youtu.be/{text}"
    else:
        return None



if __name__ == "__main__":
    main()
