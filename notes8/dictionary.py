# dictionaries are more powerful than tuples of course, you are able to assign keys to variables
# gets cryptic if you keep referencing [0] [1] [2] etc in a tuple "list"
# why not just say get what's stored as "name" and "house" ?

#def main():
#    student = get_student()
#    print (f"{student['name']} from {student['house']}") #single quotes in double quotes to avoid confusing python

#def get_student():
#    student = {} #creating a storage for "name" and "house"
#    student["name"] = input("Name: ")
#    student["house"] = input("House: ")
#    return student

# you don't have to create an empty list to store the dictionary, you can consolidate in one statement

#    name = input("Name: ")
#    house = input("House: ")
#    return {"name": name, "house": house} # earlier dictionary lesson, grabbing from list and returning the selection on the fly
                                        # nice for compact lists that don't ahve too much to store

# either way works, one is not necessarily beter than the other

#if __name__ == "__main__":
#    main()

# again, lists are mutable, similarly to a tuple, you can set a condition

#def main():
#    student = get_student()
#    if student["name"] == "Padma":
#        student["house"] = "Ravenclaw"
#    print (f"{student['name']} from {student['house']}")

#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return {"name": name, "house": house}


#if __name__ == "__main__":
#    main()


# class is like a blueprint of data objects
# you can define and give a name, essentially you are inventing your own data type in python
class Student: # we invented a new data type called "Student"; for Student, we created objects student.name
    ... # ... just means placeholder; as of now it does exist for Student class

def main():
    student = get_student()
    print (f"{student.name} from {student.house}")

def get_student():
    student = Student() # grabs the "function" created for class Student
    student.name = input("Name: ") # giving student a name     "." acts as a storage or "in", similar to [] {} for lists
    student.house = input("House: ")
    return student # class, within object oriented programming, is very powerful in that you stored 1 variable student in Student and returning that variable at the same time

if __name__ == "__main__":
    main()

# whenever you create a class and use them, you end up creating an object
