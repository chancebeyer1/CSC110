first = input("Input first name ")
middle = input("Input middle initial ")
last = input("Input last name ")

user = (first[0:3]) + middle + (last[len(last)-3:len(last)])
print("Username:", user)