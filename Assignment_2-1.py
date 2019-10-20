heightLenStr = eval(input("Type a height for a rectangle"))
while heightLenStr <= 0:
    if heightLenStr <= 0:
        print("Error! Number must be positive")
        heightLenStr = eval(input("Type a height for a rectangle"))
widthLenStr = eval(input("Type a width for a rectangle"))
while widthLenStr <= 0:
    if widthLenStr <= 0:
        print("Error! Number must be positive")
        widthLenStr = eval(input("Type a width for a rectangle"))
area = heightLenStr * widthLenStr
print("The area of a rectangle with the given height", (heightLenStr), "and the given width", (widthLenStr), "is", (area))