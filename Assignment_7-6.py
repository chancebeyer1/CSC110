L = [1, 2, 3, 4, 5, 8, 7, 0, 99]
min = L[0]

for pos in range(len(L)):
    if L[pos] < min:
        min = L[pos]

print("The min is", min)