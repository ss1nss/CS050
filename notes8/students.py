# do something simple, ask a user for their name and house (we're in the hp universe :3)
# print out where that student is from
# object oriented coding

#ex 1

#name = input("name: ")
#house = input("house: ")
#print (f"{name} from {house}")

#ex 2 - defining functions to take over input

#def main():
#    name = get_name()
#    house = get_house()
#    print (f"{name} from {house}")

#def get_name():
#    return input("name: ")

#def get_house():
#    return input("house: ")

#if __name__ == "__main__":
#    main() # only call main for this file only, otherwise if you add in other libraries, going to start calling other mains

#ex 3 - define a function with 1 function to get both name and house
# tuple - another type of data in python that's a collection of values; has the spirit of a list, but is immutable - meaning that you cannot change values, variables are fixed
# lists, you can change the values in a list, like bracket 0, bracket 1, bracket 2, bracket 3, etc - can all be added/ changed
# quite simply, you would use a tuple if you have no intention of changing values or variables and you want to return multiple vairables back

#def main():
#    name, house = get_student() #1 I made a tuple for obatining both returns in the function, but a returning tuple does not have to be returned to 2 variables
#    print (f"{name} from {house}")
# instead, you can return the tuple as similar to a list per below, where each bracket will grab the corresponding "item" from the tuple
#    student = get_student()
#    print (f"{student[0]} from {student[1]}")

#def get_student():
#    name = input("name: ")
#    house = input("house: ")
#    return name, house # just so happens that my vairables within the function are the same as in main, but I could replace with n and h, but that's more cryptic
                        #1 you're not returning 2 varibles, it's 1 "tuple"
                        #1 similarly, if you made/ stored a list, you would be returning that list

#if __name__ == "__main__":
#    main()


# you would use a tuple when you know, or must have functions where a data cannot change; lists can change depnding on what is stored; tuples are used for preventative measures
# so let's five an example of tuple's immutability

def main():
    student = get_student()
    if student[0] == "Padma": #a in a list, you could jsut have it prompt house for given name, there would be no error present
        student[1] = "Ravenclaw" #a in a tuple, it will give a error reason as the inputted house must be ravenclaw
    print (f"{student[0]} from {student[1]}")

def get_student():
    name = input("name: ")
    house = input("house: ")
    #return name, house
    return [name, house] #b let's change the return to a list, now this will return the house inputted no matter what, however, Padma will always return Ravenclaw

if __name__ == "__main__":
    main()
