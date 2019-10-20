L = [2, 7, 8, 12, 2, 0, 1, 10, 8]
L.sort()

p1 = 0
p2 = len(L)
if len(L) % 2 != 0:
    pos = (len(L) - 1) / 2
    while p1 < pos:
        p1 = p1 + 1
    med = L[p1]
else:
    pos = (len(L) - 1) / 2
    while p1 < pos:
        p1 = p1 + 1
    while p2 > pos:
        p2 = p2 - 1
    x1 = L[p1]
    x2 = L[p2]
    med = (x1 + x2) / 2

print("The median is", med)