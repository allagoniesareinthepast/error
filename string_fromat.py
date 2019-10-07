class Bic:
    def __init__(self, name, color, pen_type):
        self.name = name
        self.color = color
        self.pen_type = pen_type

    def disp(self):
        return "Pen Info : %s" % (self.name, self.color, self.pen_type)


p2 = Bic("sign pen", "black", "ball")
print(p2.disp()) # TypeError: not all arguments converted during string formatting