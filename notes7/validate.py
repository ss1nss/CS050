# regular expressions, otherwise known as regex/ regexes, really just a pattern — common in programming to match off data — often user input
# ex: for emails, make sure the use typed in an eligible email into address
# let's make a program, for yes or no, if an email is valid

email = input("What's your email? ").strip()

# for emails, @ sign is needed in the input; not the best way to determine if email
# what if user typed just @, that would be valid, which is wrong
# even though you added a ".", you would still have the prior problem; rather, you want to find the "." before the domain name

#if "@" and "." in email:
#    print("Valid")
#else:
#    print("Invalid")


# remake the code
username, domain = email.split("@") # rewrite the code splitting the @ and .

#if username and ("." in domain): # when you write the expression and "." in domain, it's only referring to the end boolean for in domain, not username
if username and domain.endwith(".edu")
    print("Valid")
else:
    print("Invalid")

# of coursem we can keep adding in more lines of code to make certain only emails are inputted, but this is going to take too much time and effort to do
