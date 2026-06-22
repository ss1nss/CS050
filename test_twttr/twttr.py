def main():

    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    letters = ""
    for not_vowels in word:
        if not_vowels not in vowels:
                letters += not_vowels
    return(letters)

if __name__ == "__main__":
    main()
