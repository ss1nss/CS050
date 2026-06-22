# let's generate a random number from 1 to 10

#import random

#number = random.randint(1, 10) # randing just means random int
#print(number)

# let's shuffle cards

import random

cards = ["jack", "queen", "king"] # you an make this list shuffle cards however you want
random.shuffle(cards)
for card in cards:
    print(card) # can't just say print card, otherwise it will print out the list as is, we want to have the cards shuffled and list the cards randomly
