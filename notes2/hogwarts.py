# I'm gonna make a list of vairables for sutdents
students = ["Hermione", "Harry", "Ron"]

# how do I print specific students?
# first list item is 0, so you can specify the print with the brack and number
#print(students[0])
#print(students[1])
#print(students[2])

# we can make this code bettter by specifying the variable within the list, instead of printing 3x, by listing the list we print out whatever is inside it
# we are not using _ (loop) but calling the variable for what it really is; the "student" in the "students" list
#for student in students:
#    print(student)

# now let's suppose we want to print the students per their logical number, 0-1-2
# you cannot use student in range of students because range uses integers
#for student in range(students)

# len or lenth allows you to list a string to get the range of values, I'll change student to i now since it's now a number due to len
for i in range(len(students)):
#   print(students[i])

#if you wanted to get the top three in the range of the list converted by len with their associated rank, you can use i+1 (because it's weird to start off at 0 if not pythonic), students[i]
   print(i+1, students[i])
