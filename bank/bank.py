# write if statements for $0 if line starts with hello, $20 if line begins with h, $100 if none are present

a = input("Greeting: ").lstrip().rstrip().lower()

if a.startswith("hello"):
    print("$0")
elif a.startswith("h"):
    print("$20")
else:
    print("$100")
