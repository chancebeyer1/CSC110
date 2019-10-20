class Dia:
    def __init__(self, caret, cut, price):
        self.caret = caret
        self.cut = cut
        self.price = price

    def __repr__(self):
        return str(self.__dict__)