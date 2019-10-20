total = 0
num = 0
while num <= 50:
    if num % 2 != 0:
        total = total + num
    num = num + 1


print("Sum:", total)


# For loop
total = 0
for num in range(1, 51, 2):
    total = total + num

print("Sum:", total)