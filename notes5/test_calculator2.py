# now we can test the square() function

#from calculator2 import square

#def main():

#    test_square()

#def test_square(): # originally, to test the function, is by constantly running the code manuually, but real world, let's remove the human from the equation
#    if square(2) != 4:
#        print("2 squared was not 4")
#    if square(3) != 9:
#        print("3 squared was not 9")
# 2 with my code for checking my calculator has limitations, what if I inputted addition in my calculator, wel 2 + 2 = 2 * 2
# also, the code I wrote for testing is longer than the actual code I wrote, always best to have fewer lines

#you can use a key-word, assert, meaning assert something as true

#def test_square():
#    assert square(2) == 4
#    assert square(3) == 9

# if run, will give AssertionError, substitute with try: and except: key-words where you usually see these error messages generated

#def test_square():
#    try:
#        assert square(2) == 4
#    except AssertionError:
#        print("2 squared was not 4")
#    try:
#        assert square(3) == 9
#    except AssertionError:
#        print("3 squared was not 9")
#    try:
#        assert square(-2) == 4
#    except AssertionError:
#        print("2 squared was not 4")
#    try:
#        assert square(-3) == 9
#    except AssertionError:
#        print("3 squared was not 9")
#    try:
#        assert square(0) == 9
#    except AssertionError:
#        print("0 squared is not 0")

#if __name__ == "__main__":
#    main()

# this is better, but it's still a lot of code for test cases
# we are also still getting 2 + 2 = 2 * 2, but at least -2 + -2 != -2 * -2

#pytest, a library that tests your code
#unit testing - is typically tests for functions you have written

# let's rewrite the code using pytest (pip install pytest)

import pytest # you can actually import the pytest library, there is a function inside called "raises" and you can raise the errors

from calculator2 import square

#def test_square():
#    assert square(2) == 4
#    assert square(3) == 9
#    assert square(-2) == 4
#    assert square(-3) == 9
#    assert square(0) == 0

# no need for main, conditional, try, prints as pytest will automate the test for me and whether or not they fail
# you run pytest name.py
# pytest will not necessarily tell you why it failed, but it will give you the error at the assert
# at the moment, the test is just on the main function, not on the user inputs liek if they type in a string like "cat"
# it's always best if you don't group everything in a main, that a function is testable, which n * n is
# once the pytest runs, the first failure stops the check

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError): # example here with pytest library raising the error generated if you try and process cat * cat
        square("cat")

# you can separate the definitions as oytest functions in each definition, so multiple definitions will give multiple tests
# so in total 2 definitions failed (positive and negative, calculator2.py is set as addition, 3 + 3 != 3 * 3 //// -2 + -2 != -2 * -2) and 1 passed (the 0 one)
# you can make multiple files to run different definitions of tests, up to you if it's convenient
# floats are vey difficult to test for
