class Diamonds:
    def __init__(self, num, caret, cut, color, clarity, depth, table, price, x, y, z):
        self.num = num
        self.caret = caret
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.price = price
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return str(self.__dict__)