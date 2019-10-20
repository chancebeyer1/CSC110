import math

L = [1, 3, 2, 4, 9, 1, 4, 10, 3, 6, 2]

H = []
for pos in range(len(L)):
    if L[pos] % 2 == 0:
        num = L[pos]
        H + num
print(H)

#   The sum
count = 0
for pos in range(len(L)):
    count = count + L[pos]

print("The sum is", count)


#   The average
avg = count / len(L)

print("The average is", avg)


#   The variance
Var1 = 0
for pos in range(len(L)):
    x = (L[pos] - avg)
    Var1 = Var1 + (x * x)
Var = Var1 / len(L)

print("The variance is", Var)


#   The Std. Deviation
StdDev = math.sqrt(Var)
print("The standard deviation is", StdDev)


#   The maximum
max = L[0]

for pos in range(len(L)):
    if L[pos] > max:
        max = L[pos]

print("The max is", max)


#   The minimum
min = L[0]

for pos in range(len(L)):
    if L[pos] < min:
        min = L[pos]

print("The min is", min)


#   The difference between max and min

dif = max - min
print("The difference between the max and min is", dif)


#   The median
L.sort()

p1 = 0
p2 = len(L)
if len(L) % 2 != 0:
    pos = (len(L) - 1) / 2
    while p1 < pos:
        p1 = p1 + 1
    med = L[p1]
else:
    pos = (len(L) - 1) / 2
    while p1 < pos:
        p1 = p1 + 1
    while p2 > pos:
        p2 = p2 - 1
    x1 = L[p1]
    x2 = L[p2]
    med = (x1 + x2) / 2

print("The median is", med)


# Question 9
K = []

for pos in range(len(L)):
    if L[pos] > avg:
        K.append(L[pos])

print(K)

#   Question 10
K = []

for pos in range(len(L)):
    if (L[pos] - avg) <= StdDev:
        K.append(L[pos])

print(K)