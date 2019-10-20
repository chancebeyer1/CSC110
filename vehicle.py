class Vehicle:
    def __init__(self, manufacturer, displ, year, cyl, trans, drv, cty, hwy, fl, cls):
        self.manufacturer = manufacturer
        self.displ = displ
        self.year = year
        self.cyl = cyl
        self.trans = trans
        self.drv = drv
        self.cty = cty
        self.hwy = hwy
        self.fl = fl
        self.cls = cls

    def __repr__(self):
        return str(self.__dict__)
