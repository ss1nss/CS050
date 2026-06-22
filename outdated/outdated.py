months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

while True:
    try:
        input_date = input("Date: ").strip()
        if "," in input_date:
            mmdd, yyyy = input_date.split(", ")
            mm, dd = mmdd.split(" ")
            mm = months.index(mm) + 1
            if int(mm) > 12 or int(dd) > 31:
                raise ValueError
            else:
                print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
                break
        elif "/" in input_date:
            mm, dd, yyyy = input_date.split("/")
            if int(mm) > 12 or int(dd) > 31:
                raise ValueError
            else:
                print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
                break
    except EOFError:
        break
    except (ValueError, KeyError, IndexError):
        pass

