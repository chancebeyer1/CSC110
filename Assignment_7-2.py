L = [1, 2, 3, 4, 5]

count = 0
for pos in range(len(L)):
    count = count + L[pos]

avg = count / len(L)

print("The average is", avg)