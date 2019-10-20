#   Question 1
#   Returns the maximum of two numbers
def max(a, b):
    if a > b:
        return a
    else:
        return b

#   Question 2
#   Returns the minimum of two numbers
def min(a, b):
    if a < b:
        return a
    else:
        return b

#   Question 3
#   Returns the cube of the given number
def cube(a):
    return a * a * a

#   Question 4
#   Determines if a number is even
def isEven(a):
    if a % 2 == 0:
        return True
    else:
        return False

#   Question 5
#   Determines if a number is odd
def isOdd(a):
    if a % 2 != 0:
        return True
    else:
        return False

#   Question 6
#   Returns the area of the rectangle
def rectArea(width, height):
    area = width * height
    return area

#   Question 7
#   Returns the surface area of a sphere with a given radius
def sphereArea(radius):
    import math
    area = 4 * math.pi * (radius * radius)
    return area

#   Question 8
#   Returns the volume of a sphere with a given radius
def sphereVolume(radius):
    import math
    volume = (4 / 3) * math.pi * cube(radius)
    return volume

#   Question 9
#   Ruturns the volume of a cylinder with a given radius and height
def cylinderVolume(radius, height):
    import math
    volume = math.pi * (radius * radius) * height
    return volume

#   Question 10
#   Returns the sum of the integers up till n
def sum(n):
    sum = 0
    for i in range(n):
        sum = sum + i
    return sum
