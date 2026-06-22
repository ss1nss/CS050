def main():
    x = input("Fraction: ")
    print(get_percent(convert(x)))

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError

        if 0 <= x / y <= 1:
            return int((x / y) * 100)
        else:
            raise ValueError
    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
        if percentage <= 1:
            return("E")
        elif 99 <= percentage <= 100:
            return("F")
        else:
            return f"{percentage}%"

if __name__ == "__main__":
    main()
