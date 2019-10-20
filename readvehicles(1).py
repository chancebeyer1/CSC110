import vehicle
import point

#   takes one line of the file and creates a vehicle object from it
def makeVehicle(line):
    manufacturer = line[3:19].strip()
    displ = eval(line[19:22].strip())
    year = int(line[22:27].strip())
    cyl = int(line[27:31].strip())
    trans = line[31:42].strip()
    drv = line[42:46].strip()
    city = eval(line[47:50].strip())
    hwy = eval(line[50:54].strip())
    fl = line[54:57].strip()
    cls = line[57:].strip()
    return vehicle.Vehicle(manufacturer,
        displ, year, cyl, trans, drv, city, hwy, fl, cls)

#   reads a file and returns a list of vehicles
def readVehicles(fileName):
    f = open(fileName)
    lines = f.readlines()
    f.close()
    vehicles = []
    #   skip the first line so start at 1
    for pos in range(1, len(lines)):
        line = lines[pos]
        v = makeVehicle(line)
        vehicles.append(v)

    return vehicles

def combinedMileage(a):
    city = a.cty
    hwy = a.hwy
    return (city + hwy) / 2

# v = vehicle.Vehicle("audi", 1.8, 1999, 4, "auto(l5)", "f", 18, 29, "p", "compact")
# w = vehicle.Vehicle("audi", 2.8, 1999, 4, "manual(m5)", "f", 21, 29, "p", "compact")
# u = vehicle.Vehicle("chevy", 4.8, 1999, 4, "manual(m5)", "f", 12, 15, "p", "sports")

# p = point.Point(10, 12)
# q = point.Point(5, 7)
# x = p
# print(p)
# print(q)
# print(x)

# LL = [ p, q]

# for pos in range(len(L)):
#     #   x is the pos-th vehicle in the list L
#     x = L[pos]
#     cm = combinedMileage(x)
#     print(cm)

def findDisplacement(L, upper):
    K = []
    for pos in range(len(L)):
        #   x is the pos-th vehicle in the list L
        x = L[pos]
        if x.displ < upper:
            K.append(x)

    return K

L = readVehicles("/home/graham/Courses/110/highway.txt")

import listfuncs
hwys = []
for pos in range(len(L)):
    v = L[pos]
    hwys.append(v.hwy)
avgHwy = listfuncs.average(hwys)
print(avgHwy)

avgHwy = listfuncs.average([v.hwy for v in L])
print(avgHwy)


# K = findDisplacement(L, 2)
# print(len(K))
#
# for v in K:
#     print(v)

# L = [ v, w, u ]
# print(v)
# print(L)
# d = findDisplacement([ v, w, u ], 3)
# print(d)
