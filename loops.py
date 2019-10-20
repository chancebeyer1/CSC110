# Number loop
# 1 Eveluates the condition
# 2 if condition is true
#   a) executes the body of the loop
#   b) go back to step 1
# 3 if condition is false skips the while loop


# i = 1
# while i <= 10:
#     print(i)
#     i = i + 2

# i = 5
# while i <= 100:
#     print(i)
#     i = i + 5


# total = 0
# num = 1
# while num <= 100:
#     total = total + num
#     num = num + 1
#
# print(total)

# total = 0
# num = 1
# while num <= 100:
#     if num % 2 == 0:
#         total = total - num
#     else:
#         total = total + num
#     num = num + 1
#
# print(total)

# total = 1
# num = 2
# while num <= 100:
#     total = total + num
#     num = num + 1
#
# print(total)
#
# print(2.2 - 3.2)


M = 4
N = 126
i = M
pos = 1
total = i
while i < N:
    if total % 2 == 0:
        total = total - (M+pos)
        pos = pos + 1
    else:
        total = total + (M+pos)
        pos = pos + 1
    i = i + 1
total = total - N
print(total)