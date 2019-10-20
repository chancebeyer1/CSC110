L = [3, 4, 5, 8, 7]
max = L[0]
min = L[0]

for pos in range(len(L)):
    if L[pos] > max:
        max = L[pos]

for pos in range(len(L)):
    if L[pos] < min:
        min = L[pos]

dif = max - min
print("The difference between the max and min is", dif)