L = [1, 2, 3, 4, 5]

count = 0
for pos in range(len(L)):
    count = count + L[pos]

avg = count / len(L)
Var1 = 0
for pos in range(len(L)):
    x = (L[pos] - avg)
    Var1 = Var1 + (x * x)

Var = Var1 / len(L)
print("The variance is", Var)