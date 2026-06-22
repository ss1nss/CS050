import sys
import re
import validators
import random
import cowsay

# Define the foods and their calorie values
foods = {
    "apple": {"calories": 95, "ingredients": ["fiber", "vitamin C"]},
    "banana": {"calories": 105, "ingredients": ["potassium", "vitamin B6"]},
    "burger": {"calories": 354, "ingredients": ["protein", "fat"]},
    "pizza": {"calories": 285, "ingredients": ["carbohydrates", "protein"]}
}

# Function to select difficulty
def select_difficulty():
    while True:
        try:
            difficulty = int(input("Select difficulty (1-3): "))
            if difficulty in [1, 2, 3]:
                return difficulty
            else:
                print("Please select a valid difficulty level (1-3).")
        except ValueError:
            print("Please enter a number (1-3).")

# Function to determine boss health based on difficulty
def boss_health(difficulty):
    base_health = 10
    return base_health * difficulty

# Function to simulate an attack
def attack(food_calories):
    damage = food_calories * 0.01
    return damage

# Function to simulate a run action
def run():
    print("You tried to run away, but the boss is too fast!")
    return 0

# Function to simulate a defend action
def defend():
    print("You defended against the boss's attack!")
    return -5

# Function to display attack, run, defend options
def attack_run_defend():
    options = ["attack", "run", "defend"]
    cowsay.cow("Choose an action: " + ", ".join(options))
    while True:
        choice = input("Attack, Run, or Defend? ").lower()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please choose again.")

# Main game loop
def main():
    difficulty = select_difficulty()
    boss_hp = boss_health(difficulty)
    print(f"Boss Health: {boss_hp}")

    while boss_hp > 0:
        choice = attack_run_defend()

        if choice == "attack":
            food = random.choice(list(foods.keys()))
            food_calories = foods[food]["calories"]
            damage = attack(food_calories)
            boss_hp -= damage
            print(f"You attacked with {food} causing {damage:.2f} damage! Boss Health: {boss_hp:.2f}")

        elif choice == "run":
            run_damage = run()
            boss_hp -= run_damage
            print(f"Boss Health: {boss_hp:.2f}")

        elif choice == "defend":
            defend_damage = defend()
            boss_hp += defend_damage
            print(f"Boss Health: {boss_hp:.2f}")

        if boss_hp <= 0:
            print("Victory! You defeated the boss!")
            break
        else:
            print("The battle continues!")

if __name__ == "__main__":
    main()
