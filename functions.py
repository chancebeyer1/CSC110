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

def square(x):
    return x * x

def cube(x):
    return square(x*x)

def fourth(x):
    return square(square(x))

def pow(x, n):

    result = 1
    for i in range(n):
        result = result * x


def areaUnderCurve(a, b, N, f):

    width = (b-a) / N

    total_area = 0

    c = a
    while c < b:
        height = f(c)
        area = width * height
        total_area = total_area + area
        c = c + width
    return total_area
