import vehicle
import point


p = point.Point(10, 12)
def averageMilage(a):
    city = a.cty
    hwy = a.hwy
    return (city + hwy) / 2
v = vehicle.Vehicle("audi", 1.8, 1999, 4, "auto(15)", "f", 18, 29, "p", "compact")
w = vehicle.Vehicle("audi", 1.8, 1999, 4, "auto(15)", "f", 21, 29, "p", "compact")
u = vehicle.Vehicle("chevy", 4.8, 1999, 4, "man(15)", "f", 18, 29, "p", "compact")

L = [v, w, u]
print(v)

cmv = combinedMileage(v)
print(cmv)

# K = []
# for pos in range(len(L))
#     x = L[pos]
#     if x.displ < 3:
#         K.append(x)