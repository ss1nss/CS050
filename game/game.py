import random

guessed = False

while not guessed:
    try:
        level = int(input("Level: "))
        n = random.randint(1, level)
        while True:
            guess = int(input("Guess: "))
            if guess < n:
                print("Too small!")
            elif guess > n:
                print("Too large!")
            elif guess == n:
                print("Just right!")
                guessed = True
                break
    except ValueError:
        pass
    except EOFError:
        break

