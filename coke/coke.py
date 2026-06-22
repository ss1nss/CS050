def main():
        coke = int("50")
        print("Amount Due:", coke)
        coins = int(input("Insert Coin: "))
        while coins != 5 and coins != 10 and coins != 25:
                print("Amount Due:",coke)
                coins = int(input("Insert Coin: "))
        change(coke, coins)

def change(coke, coins):
        print("Amount Due:", int(coke) - int(coins))
        while coke > coins:
                coke -= coins
                coins = int(input("Insert Coin: "))
                if coke - coins == 0:
                        print("Change Owed: 0")
                elif coke > coins:
                        print("Amount Due:", int(coke) - int(coins))
        if coins > coke:
                print("Change Owed:", int(coins) - int(coke))


main()
