# pre-made template, fill in time and conver to actual number which wil lbe used to give eating times; resutls outside of the conversion will result in nothing

def main():
    eat = (input("What time is it? "))
    n = convert(eat)
    if 7 <= n <= 8:
        print("breakfast time")
    elif 12 <= n <= 13:
        print("lunch time")
    elif 18 <= n <= 19:
        print("dinner time")
    else: ""
#    print(n) #just to check is decimlas pop out

def convert(time):
    if "a.m." in time or "p.m." in time:
        time_frame, m = time.split(" ") # adding space between objects
        hours, minutes = time_frame.split(":") # adding : between 1st object
        if "p.m." == m and 12 != int(hours): # if condition is filled for army time
            time = int(hours) + 12 + int(minutes)/60 # then add the hours to the clock
        else:
            time = int(hours) + int(minutes)/60 # otherwise leave as is
        return time

    else:
        hours, minutes = time.split(":")
        time = int(hours) + int(minutes)/60
        return time


if __name__ == "__main__":
    main()
