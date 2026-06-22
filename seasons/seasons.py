from datetime import date, datetime
import sys
import inflect

p = inflect.engine()

def main():

    if len(sys.argv) > 1:
        season = " ".join(sys.argv[1:])
    else:
        season = (input("Date of Birth: "))
    try:
        today = date.today()
        dob = date.fromisoformat(season)
        days = (today - dob).days
        print(change(days))
    except ValueError:
        sys.exit("Invalid Date")


def change(s):
        minutes = s * 24 * 60
        return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"



if __name__ == "__main__":
    main()
