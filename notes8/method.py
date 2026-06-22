# calling the class like, student.name / house is still very manual
# classes come with certain methods, or functions, inside of them and they behave in special ways due to the nature of how python works

class Student:
    def __init__(self, name, house): # __init__ is a method (aka dunder init method), is known as an instance method and it's just called this so that you can initialize contents of an object from a class
                        # what is this?? similar to adding keys to dictionaries, this is adding variables to objects
                        # instance variables to objects
                        # self needs to be in there, even though it makes more sense to just say student, house; self is the storage
                        # you can call it anything you want, but it must always come first, and conventionally it's called self
                        # python will automatically store the information for you throguh the referenced argument
        self.name = name # ie - you can create the attributes to store, self.name is this particular name same for house
        self.house = house


def main():
    student = get_student()
    print (f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) # instead, I am calling the capital S attribute for student to give me the particular name and house; more control of what I want returned
                # this is a constructor call, line of code constructs a Student object for me; using Student class as a template
                # similar to a house, it can be different colors, shapes sizes etc, but for student, we're giving it a blueprint for name/ house
                # def is alwayus called by a function called __init__ ; the initialization of an object
    return student

if __name__ == "__main__":
    main()


