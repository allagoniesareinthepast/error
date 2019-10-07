class Bic:
    def __init__(self, name, color, pen_type):
        self.name = name
        self.color = color
        self.pen_type = pen_type

    def disp(self):
        # format해야할 attribute는 3개인데, %s를 하나만 적어줘서... 갯수를 맞추고 해결함.
        return "Pen Info : %s, %s, %s" % (self.name, self.color, self.pen_type)


p2 = Bic("sign pen", "black", "ball")
print(p2.disp())  # TypeError: not all arguments converted during string formatting
