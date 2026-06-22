import re
import sys


def main():
    if len(sys.argv) == 1:
        print(validate(input("IPv4 Address: ")))
    elif len(sys.argv) == 2:
        print(validate(sys.argv[1]))

def validate(ip):
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        octects = ip.split(".")
        for octet in octects:
            if not 0 <= int(octet) <= 255:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()
