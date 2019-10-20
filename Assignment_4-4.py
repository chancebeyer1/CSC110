def f(x):
    return x * x

a = 10
b = 40
N = int(input("Input number of triangles "))

width = (b-a) / N
total = 0
c = a
d = a + width
while c < b:
    height_1 = f(c)
    height_2 = f(d)
    area = ((height_1 + height_2) / 2) * width
    total = total + area
    c = c + width
    d = d + width
print("Area", total)