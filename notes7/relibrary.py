# re = library we can use to fix that email kind of problem

# re.search(pattern, string, flags=0) # pattern can intake numerous special symbols

# . = any character except a new line
# * = 0 or more repetitions, acceptable for 0 or more
# + = 1 or more repetitions, at least 1 or more
# ? = 0 or 1 repetition, only 0 or 1
# {m} = m repetitions, up to upper limit of repetitions
# {m,n} = m through n repetitions, range of repetitions
# ^ = matches the start of the string, strips the beginning of the string; not exactly strip, but saying this is the beginning
# $ = matches the end of the string or just before the newline at the end of the string, strips the end of the string; no exactly strip, but saying that this is the end
# [] = set of characters, "these" characters are allowed
# [^] = complementing the set, "these" characters are not allowed
# \d decimal digit
# \D not a decimal digit
# \s whitespace character
# \S not a white space character
# \w word character ... as well as numbers and underscore
# \W not word character etc

import re

email = input("What's your email? ").strip()

#if re.search(".+@.+", email): # pattern = aaa@aaa.com; so you would use .+ then .+
                                # but right now this code is saying, "you need 1 of any character before @ and 1 of any character after @
#if re.search("..*@..*", email): # so, another way of doing it ..*, any character, then any character from 0+ repetitions, works the same way
                # any character + any characters with 1 or more repetitions, @ symbol, then repeat, is valid for emails
#if re.search(r".+@.+\.edu", email): # so if you want to add in a ".edu" check, you have to escape from the re with a "\"; you need to use r to tell that we are using regular expression but \ is active
                # r string works similarly to the f string, right after the \, the character is not a special character part of re
#    print("Valid")
#else:
#    print("Invalid")

#if re.search(r"^.+@.+\.edu$", email): # pretty much preventing if someone said "my email is xyz@gmail.com yo" /// ^ and $ acts as a strip
                # removing trailing space with ^ and $, any characters with 1+ repetitions before @ symbol, then any characters after with 1+ repetions, ending in a .edu
#    print("Valid")
#else:
#    print("Invalid")


# Let's use the [] and [^] to specify more limitations for inputted emails
#if re.search(r"^[^@]+@[^@]+\.edu$", email):
                # [^@] this is the set of characters without an @ sign, remove the "." as [] takes it's place
#    print("Valid")
#else:
#    print("Invalid")

# Let's use the [] and [^] to specify more limitations for inputted emails
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
                # [] allows for ranges of characters to be included or allowed in the input, + allows for at least 1 input to unlimited
#    print("Valid")
#else:
#    print("Invalid")

# You don't have to type out the ranges, chances are, someone or a lot of people had this same issue, so? take advantage of the re's available
#if re.search(r"^(\w|\s)+@\w+\.edu$", email):
                # \w = any word or character; + = 1 or more
                # (\w|\s) = can contain any word or space
#    print("Valid")
#else:
#    print("Invalid")


# There's still a problem, .edu specifies lowercase, you could add .lower() to the user's input; but we can use the 3rd option of re.search(pattern, string, flag), set teh flag

# re.IGNORECASE ignores cases
# re.MULTILANE maybe user's inputs multiple lines, like not just his email, but wrote an entire paragraph and you want to amtch each line
# re.DOTALL configure the dot to recognize not just any character except new lines, but any character plus new lines as well

if re.search(r"^(\w|\s)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
                # \w = any word or character; + = 1 or more
                # (\w|\s) = can contain any word or space
                # (\w+\.)? = any word character ending in a period with 0 or 1 repetitions, this makes it optional for having another period sentence; like someone@cs50.harvard.edu
    print("Valid")
else:
    print("Invalid")

# okay, though we wrote code to intake emails, there's still a lot of cases we need to take into account for acceptable emails; however, many coders alrady faced this problem
# do not have to reinvent the wheel, there's already a library

# besides re.search(pattern, string, flag), there's re.match(pattern, string, flag) and re.fullmatch(pattern, string, flag)
# re.match() does not require the ^ symbol, re.fullmatch already contains ^ and $
