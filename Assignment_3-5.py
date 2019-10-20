initialNum = eval(input("Enter how many numbers to sum "))
total = 0
while initialNum > 0:
    num = eval(input("Enter a number "))
    total = total + num
    initialNum = initialNum - 1

print("The sum of those numbers is ", total)