# so far we made code with data that stores in memory
# after running/ finishing the program, the data is then lost
# let's think about lists

#names = [] # normally, you just prompt the user and user's prompt = answer; with a list you can store inputted names

#for _ in range (3): # as always, _ just means a "throwaway" variable; it holds no meaning except to signify the variable has no purpose (it can be _, i, any variable you want)
    #name = input("What's your name? ")
    #print(f"hello, {name}")

#    names.append(input("What's your name? ")) # a more pythonic/ efficient way of writing the above prompt, we want to append the list of names

#for name in sorted(names):
#    print(f"hello, {name}")

# when the above code is run, names are stored but once the prompts finish and prints, the next time you open the program, those saved names are gone
# this would be very painful to have to tenter names again and again

# File IO/ Files = ways to store information persistently, whether on PC db, cloud, usb, etc.


# open writes/ reads information from the file, formally, waht you want to open, and how you want to open it

#name = input("What's your name? ")

#file = open("names.txt", "a") # names.txt if the name of the file I want to store the names in, which you can call anything you want, but in this case you are storing text
# w stands for write, as in, you want to write information in the program // w opens the content in a way you can change the content
## if I change the w (write) to a (append), you can save information from prior oppenings of the file
## above code does not break the lines for new inputs

#file.write(f"{name}\n") ## \n will line break each time you enter a name
#file.close() # you don't write close like so normally in pythonic ways, people may forget to close the file

# these 3 file programs are like double clicking a program, like microsoft word, then saving and closing it
# currently, if the program is ran, it will recreate the file, rather than appending the information


# Rewriting the program above but more pythonic
# "with" can replace file.close(), you don't have to call for lcose, instead you can say "with open()" = I want you to open and close files automatically

name = input("What's your name? ")
with open("names.txt", "a") as file: # shift the variable to the end, "as x" = just the way the code is, no reason really
    file.write(f"{name}\n")


# all we've done is write names to the file, how do we read them back?
