L = [ 2, 3, 7, 2, 1, 9]

sum = 0
for pos in range(len(L)):
    num = L[pos]
    sum = sum + num

print(sum)

sum = 0
for x in L:
    sum = sum + x

print(sum)

avg = sum / len(L)

print(avg)

varSum = 0
for pos in range(len(L)):
    num = L[pos]
    sq = (num - avg) ** 2
    varSum = varSum + sq

variance = varSum / len(L)

print(variance)

import math
stddev = math.sqrt(variance)
print(stddev)

max = L[0]
for pos in range(len(L)):
    num = L[pos]
    if num > max:
        max = num

print(max)

min = L[0]
for pos in range(len(L)):
    num = L[pos]
    if num < max:
        min = num

print(min)

print(max-min)

L.sort()
if len(L) % 2 == 0:
    #   even length
    medPos = len(L) // 2
    median = (L[medPos] + L[medPos - 1]) / 2
else:
    medPos = len(L) // 2
    median = L[medPos]

print(median)

K = []
for pos in range(len(L)):
    num = L[pos]
    if num > avg:
        K.append(num)

print(K)

K = []
for pos in range(len(L)):
    num = L[pos]
    if num > avg - stddev and num < avg + stddev:
        K.append(num)

print(K)