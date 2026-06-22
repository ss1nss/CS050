# logic of and, let's assume we are grading papers
score = int(input("Score: ")) # user inputs whatever grade/ points they received

#if score >= 90 and score <= 100:
#    print("Grade: A")
#elif score >= 80 and score < 90:
#    print("Grade: B")
#elif score >= 70 and score < 80:
#    print("Grade: B")
#elif score >= 60 and score < 70:
#    print("Grade: B")
#else:
#    print("Grade: F")

# let's simplify the wording to have a more concise code
# we can instead say number <= score and less than (or equal to for the first grade) number
#if 90 <= score <= 100:
#    print("Grade: A")
#elif 80 <= score < 90:
#    print("Grade: B")
#elif 70 <= score < 80:
#    print("Grade: C")
#elif 60 <= score < 70:
#    print("Grade: D")
#else:
#    print("Grade: F")

# we can make this simpler, we don't have to have 2 numbers
# do not need the lower bound and upper bound to be asked each time, if lower is less than the number stated it goes "else"where
# again, el stops the code if it is true in that parameter
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
