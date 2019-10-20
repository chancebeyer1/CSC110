import random
import math

N = 100000000
count = 0

for i in range(N):
    x = random.random()
    y = random.random()
    if math.sqrt(x*x + y*y) <= 1:
        count = count + 1
print(4 * count)