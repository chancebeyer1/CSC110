def max(a, b):
    if a > b:
        return a
    else:
        return b

def min(a, b):
    if a < b:
        return a
    else:
        return b

def cube(x):
    return x * x * x

def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

def isEven(x):
    return x % 2 == 0

def isOdd(x):
    if x % 2 == 1:
        return True
    else:
        return False

def isOdd(x):
    return x % 2 == 1

def isOdd(x):
    return not isEven(x)

def rectArea(w, h):
    return w * h

def sphereArea(r):
    import math
    return math.pi * r * r * 4

def sphereVolume(r):
    import math
    return math.pi * r * r * r * 4 / 3

def cylinderVolume(r, h):
    import math
    return math.pi * r * r * h

def sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s