#   Question 1
def maxL(L):
    max = L[0]
    for pos in range(len(L)):
        if L[pos] > max:
            max = L[pos]
    return max

#   Question 2
def minL(L):
    min = L[0]
    for pos in range(len(L)):
        if L[pos] < min:
            min = L[pos]
    return min

#   Question 3
def spread(L):
    dif = max(L) - min(L)
    return dif

#   Question 4
def sumL(L):
    sum = 0
    for pos in range(len(L)):
        sum = sum + L[pos]
    return sum

#   Question 5
def average(L):
    avg = sum(L) / len(L)
    return avg

#   Question 6
def variance(L):
    Var1 = 0
    for pos in range(len(L)):
        x = (L[pos] - average(L))
        Var1 = Var1 + (x * x)
    Var = Var1 / len(L)
    return Var

#   Question 7
def stddev(L):
    import math
    stddev = math.sqrt(variance(L))
    return stddev

#   Question 8
def even(L):
    H = []
    for pos in range(len(L)):
        if L[pos] % 2 == 0:
            num = L[pos]
            H.append(num)
    return H

#   Question 9
def evenPos(L):
    H = []
    for pos in range(len(L)):
        if L[pos] % 2 == 0:
            H.append(pos)
    return H

#   Question 10
def allEven(L):
    H = even(L)
    return H == L