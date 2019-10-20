#   radix sort

L = [1, 5, 6, 2, 3, 4, 1, 4, 9, 2, 1]

counts = [0] * 10
for pos in range(len(L)):
    x = L[pos]
    counts[x] = counts[x] + 1


print(counts)