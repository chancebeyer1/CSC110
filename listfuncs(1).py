#   return the sum of a list of numbers L

def sum(L):
    result = 0
    for i in range(len(L)):
        num = L[i]
        result = result + num

    return result

def sum(L):
    result = 0
    for x in L:
        result = result + x

    return result

def average(L):
    return sum(L) / len(L)

#   given a list of X's and a predicate/condition function, return
#   a list of X's for which the condition is true
def filter(L, condition):
    result = []
    for v in L:
        if condition(v):
            result.append(v)

    return result