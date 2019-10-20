a = eval(input("Type the first number "))
b = eval(input("Type the second number "))
c = eval(input("Type the third number "))
# Should I be using max here instead of (a * b) > (a * c) > (b * c)?
if (a * b) > (a * c) > (b * c):
    print("The first number multiplied by the second number is largest")
else:
    if (a * c) > (b * c):
        print("The first number multiplied by the third number is largest")
    else:
        print("The second number multiplied by the third number is largest")