# whatever word is inputted, only the vowels - in whatever case - are removed; words without vowels are regurgitated
vowels = input("Input: ")
for _ in vowels: #unassigned variable task to what is inputted
    if _ in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]: #if what is inputted has a vowel
        print("", end="") #print blanks in place of _ and delete spaces
    else:
        print(_, end="") #print as is
print("")
