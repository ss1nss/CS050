# dict allows you to associate keys and values, something with something else; like word and their definitions
#Hermione == Gryffindor, Harry == Gryffindor, Ron == Gryffindor, Draco == Slytherin

# who is in which house defined by dictionary
# can do this with lists alone
#students = ["Hermione", "Harry", "Ron", "Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
# but this is incredibly inefficient, we can only associate the list per person one at a time, so that 0 in students = 0 in house, etc; so what if we had 100 students and we wanted to also associate the spells

# for dictionaries, we use curly brackets {}
# this is much simpler than before, but it can still get messy, depending on how many students need to be associated
#students = {
#    "Hermione": "Gryffindor",
#    "Harry": "Gryffindor",
#    "Ron": "Gryffindor",
#    "Draco": "Slytherin"
#}

# printing out the word, prints the definition, this works, but again it's messy in extreme cases
#print(students["Hermione"])
#print(students["Harry"])
#print(students["Ron"])
#print(students["Draco"])

# if you just type in the _ in students, you get the first key word
#for student in students:
#    print(student)

# if student is a student in student, then print the association for the _; add sep=", " to add a comma between spaces
#for student in students:
#    print(student, students[student], sep=", ")

# Now let's assume for the names, besides houses, they also have their animals
# list is defined as [], dictionary is {}, within the list, word are associated within the dictionary
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"}, #student does not have a patronus, so instead we could type None, instead of ""
]

#print everything out in the list per definition
for student in students:
    print(student["name"],student["house"],student["patronus"], sep=", ")
