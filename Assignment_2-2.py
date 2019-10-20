# Program that reads two numbers and prints out which ever one that is greater/less than, or equal to.
a = eval(input("Type the first number "))
b = eval(input("Type the second number "))
if a <= b:
    if a == b:
        print("The first number is equal to the second number")
    else:
        print("The second number is bigger than the first number")
else:
    print("The first number is greater than the second number")