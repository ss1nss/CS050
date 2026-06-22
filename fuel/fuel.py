def main():
    x = get_percent("Fraction: ")
    print(x)

def get_percent(fraction):
    while True:
        try:
            x, y = input(fraction).split("/")
            if int(x)/int(y) <= .01:
                return("E")
            elif .99 <= int(x)/int(y) <= 1:
                return("F")
            elif 0 <= int(x)/int(y) <= .98:
                return str(round((int(x)/int(y))*100)) + "%"
        except (ValueError, ZeroDivisionError):
            pass


main()
