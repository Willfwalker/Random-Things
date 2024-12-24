#Take inpunt from the user and adds them together
try:
    x = int(input("Pick a number: "))
    y = int(input("Pick another number: "))
    print("The sum is:", x + y)
#if there is an error it prints the issue
except ValueError:
    print("You put in a letter not number")
