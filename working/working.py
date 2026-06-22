import re
import sys


def main():

    if len(sys.argv) == 1:
        print(convert(input("Hours: ")))
    elif len(sys.argv) == 2:
        print(convert(sys.argv[1])) # time entered in quotes to count as the 2nd argument "5:00 AM to 9:00 PM"
    else:
        sys.exit("Not a convertable time")


def convert(s):
    match = re.match(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s)
                        # 1 or 2 digits, if : is present, grab first 2 digits, second ? makes it optional if it is there or not, ending with period then to... repeat
    if match:

        start_group = match.group(2) if match.group(2) else "00"
        end_group = match.group(5) if match.group(5) else "00"
                        # minute group will be match group if present, if not assumes 00

        minute_start = int(start_group)
        minute_end = int(end_group)

        if minute_start >= 60:
            raise ValueError
        if minute_end >= 60:
            raise ValueError

        start = convert2(int(match.group(1)), minute_start, match.group(3))
        end = convert2(int(match.group(4)), minute_end, match.group(6))

        return f"{start} to {end}"
    else:
        raise ValueError

def convert2(hour, minute, period):
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
