radiusLenStr = eval(input("Type a radius for a cylinder"))
heightLenStr = eval(input("Type a height for a cylinder"))
import math
volume = heightLenStr * radiusLenStr**2 * (math.pi)
print("The volume of a cylinder with the given radius", (radiusLenStr), "and the given height", (heightLenStr), "is", (volume))