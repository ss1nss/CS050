nutrition = [
    {"food": "Apple", "calories": "130"},
    {"food": "Avocado", "calories": "50"},
    {"food": "Sweet Cherries", "calories": "100"},
    {"food": "Tangerine", "calories": 130},
    {"food": "Green Apple", "calories": 100},
    {"food": "Banana", "calories": 150},
    {"food": "Passion Fruit", "calories": 100},
    {"food": "Lemon", "calories": 30},
    {"food": "Kiwifruit", "calories": 90},
    {"food": "Pear", "calories": 100},
]

item = input("Item: ").title().rstrip().lstrip()

for fruit in nutrition: # _ defined as fruit from the list in nutrition
    if item == fruit["food"]: # if input is the same as the category in the dictionary, print calories
        print("Calories: ", fruit["calories"])
else:
    None
