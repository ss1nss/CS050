# writing a program to store and keep adding into a file

import csv # still making a csv, import csv

name = input("What's your name? ")
home = input("Where's your home? ") # for Harry's home, if you type in his full address, it will come out as csv format which will be "Number Four, Privet Drive"

#with open("students3.csv", "a") as file:
#    writer = csv.writer(file)
#    writer.writerow([name, home]) # you want to print whatever is inputted in to the same row

#again same as with reader, writer is just for lists
# we can use DictWriter to input as dictionaries, now we have headers

with open("students3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
