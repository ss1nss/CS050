import random

def main():

    level = get_level()
    equations = 10
    chances = 3
    points = 10


    while equations != 0:

        x, y = generate_integer(level) # random equation is generated
        generated_answer = x + y

        while chances != 0:

            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == generated_answer:
                    equations -= 1
                    chances = 3
                    break # making sure I break the inner loop to generate the next equation
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                chances -= 1

        if chances == 0:
            print((f"{x} + {y} = {generated_answer}"))
            chances = 3
            points -= 1
            equations -=1
            continue

    print(f"Score: {points}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y






if __name__ == "__main__":
    main()

