# what if we not only wanted to  store people's names, but other details as well
# you can code for "names.csv"
# csv's separates values with commas, and new typoes of data with new lines
# csv's can be imported to db, like excel to read the data

#with open("students.csv") as file:
#          for line in file: # again, line and file are just variables, file given to as the name for the program, and line just as a stand in for true
#                  row = line.rstrip().split(",") # the whole line of text would be regurgitated by how the lines of codes are made; split lines where there is a comma in the csv file
                    # common to think of each line as a row, and each line with separations as column ("Hermione, Gryffindor")
#                  print(f"{row[0]} is in {row[1]}") # "Hermione is in Gryffindor" python starts with 0 as the first item again pythonic


#students = []

# above stores the "rows" in a list, you can unpack instead if you know that you just want to print the worws
#with open("students.csv") as file:
#          for line in file:
#                  name, house = line.rstrip().split(",") # where there is a comma, separtes the variables and assigns it to the variable reciprocately
                  #print(f"{name} is in {house}")
#                  students.append(f"{name} is in {house}") # so, instead let's now store in a list, why? because what if wwe want to sort the list automatically instead of manualy from the csv.

#for student in sorted(students):
#        print(student)

# above code is sloppy, not sorting by name, but by english sentence stucture
# above code is not well designed, english is read left to right, so we're getting lucky in how the names are getting printed

# create an empty dictionary that has 2 keys stored into it, name and house


# dictionary {}, list []
students = []

with open("students.csv") as file:
          for line in file:
                  name, house = line.rstrip().split(",") # still ahve the names and houses separated by the comma
#                  student = {} # temporary dictionary that stores the stuudent's name and house; dictionaries can only have strings quoted, unlike list where you can do [1 , 2, 3]; dictionaries must be ["one", "two", "three"]
#                  student["name"] = name
#                  student["house"] = house
                  student = {"name": name, "house": house} # can comibine those 3 lines above to one, make it more concise
                  students.append(student) # adding student dicitonary to the list students
# the reason why this is done, even though it's more complicated, is because we collected all infomration about students whuile still keeping track of what's name and what's house

#def get_name(student): # we are adding the name specifying sorted to sort by the student's name, conversely you can change the function to key at the house instead
#        return student["name"]
#for student in sorted(students, key=get_name): # adding in sorted to "sort" the list of stored dictionary items; we can add key to add in functions, that way sort sorts by the key added
#                                # I only want to call the function, not to perform it so no "()" added
#        print(f"{student['name']} is in {student['house']}") # reason why we are using single quotes in this dictionary, is because we are already using double quotes in the above list
                                                                # you need to tell python to differentiate between the list and dictionary; so it does not get confused what lines upp with what

# get_name function works, but we can tighten this further, as we know sorted already handles how dictionaries are laid out
for student in sorted(students, key=lambda student: student["name"]): # "key=lamba student: student["name"]" is doing the exact same thing as get_name
                                # lambda is calling each student in the list, returning each value
                                # instead of def, lambda
        print(f"{student['name']} is in {student['house']}")
