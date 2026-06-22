def main():
    x = get_price("Item: ")
    print(x)

def get_price(item_prompt):
    food = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.00

    while True:
        try:
           food_input = input(item_prompt).title().strip()
           if food_input in food:
               total += food[food_input]
               print(f"${total:.2f}")
           else:
               pass
        except EOFError:
            break
        except (KeyError):
            pass


main()
