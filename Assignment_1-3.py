baseLenStr = eval(input("Type a base for a right triangle"))
heightLenStr = eval(input("Type a height for a right triangle"))
hypotenuse = (heightLenStr**2 + baseLenStr**2)**(1/2)
print("The hypotenuse of a right triangle with the given base", (baseLenStr), "and the given height", (heightLenStr), "is", (hypotenuse))