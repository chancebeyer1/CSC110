L = [1, 2, 3, 4, 5, 8, 7, 99]
max = L[0]

for pos in range(len(L)):
    if L[pos] > max:
        max = L[pos]

print("The max is", max)