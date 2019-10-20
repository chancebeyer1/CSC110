# N = 10
# sum = 0
# i = 1
# while i <= N:
#     sum = sum + i
#     i = i + 1
# print(sum)
#
# sum = 0
# for i in range(1, N+1):
#     sum = sum + 1
# print(sum)


# Bird for loop
P = 1000
R = 10
yr = 0
while P < 50000:
    increase = P * R/100
    P = P + increase
    yr = yr + 1
print(yr)


