# a = 10
# b = 40
# Tarea = 0
# n = 10000000
# Rarea = 0
# count = 0
# range = b - a
# width = range / n
# while count <= n:
#     Rarea = (((a + width*count)**2) + 5)*width
#     Tarea = Tarea + Rarea
#     count = count + 1
#
# print(Tarea)


def f(x):
    return x*x + 5
a = 10
b = 40
N = 10

width = (b-a) / N

total_area = 0

c = a
while c < b:
    height = f(c)
    area = width * height
    total_area = total_area + area
    c = c + width
print(total_area)


