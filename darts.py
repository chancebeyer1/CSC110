import random

counts = [0] * 61

N = 1000
for i in range(N):

    d1 = random.randint(1, 20)
    d2 = random.randint(1, 20)
    d3 = random.randint(1, 20)
    total = d1 + d2 + d3
    counts[total] = counts[total] + 1

for pos in range(len(counts)):
    count = counts[pos]
    print(pos, count / N)

#
# import random
#
# N = 100000
#
#
# for target in range(3, 61):
#     count = 0
#     for i in range(N):
#         d1 = random.randint(1, 20)
#         d2 = random.randint(1, 20)
#         d3 = random.randint(1, 20)
#         total = d1 + d2 + d3
#         if total == target:
#             count = count + 1
#     prob = count / N
#     print(target, prob)