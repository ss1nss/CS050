# waht we originally did for our code was to split by "," to indicate which variables are which; however, this is goign to get complicated fast. What if a guys name was Ab,Raul as the first name?
# you cannot split by , anymore in this case
# csv library predicts this, as so many people have probably had this problem, this library was added to ease the splits

import csv

students = []

with open("students2.csv") as file:
#    reader = csv.reader(file) # instead if sav=ying something like line in file / line.split(","), replace with reader
# reader reads the csv file for you, where the commas, splits are
#    for name, home in reader: # for each row in the reader (in this case, it's 2 variables); if you know it's 2 rows, instead of stating rows, give it the 2 variables
    reader = csv.DictReader(file) #reader returns list, dictreader returns dictionaries
    for row in reader: # reverting back to row in reader
        students.append({"name": row["name"], "home": row["home"]}) # appending the reader with the dictionaries; row contains the list of name or home
        # even if the csv is in reverse, so homes then names, it will still work as names > homes, it's smart
        # let's say I added houses to the csv at the last column, well it will still work, as we are still calling the columns; not as fragile as if we were saying that this is how it should be ordered
        # for instance, calling "," as the split
        # this is because now there are header's, it does not matter so long as the variables are in the column being read, headers will read down the list
for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is from {student['home']}")
