# def f(x):
#     return (x-3) * (x-7)
#
# import random
# import math
#
# x = random.random() * 100 - 50
# while math.fabs (f(x)) > 0.0001:
#     x = random.random() * 100 - 50
#
# print(x, f(x))

def f(x):
    return (x-3) * (x-7)

import random
import math

L = -50
R = 5

while math.fabs (f(L)) > 0.0001:
    M = (L + R) / 2
    y = f(M)
    if y > 0:
        L = M
    else:
        R = M
print(L, f(L))