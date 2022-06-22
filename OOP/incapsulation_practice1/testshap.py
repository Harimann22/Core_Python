from shap import Shape


class Ractangal(Shape):

    def __init__(self, color, border_width, length, width):
        super().__init__("Green", "4545")
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width


rc = Ractangal("Red", "35", "32", "20")
# rc.set_color("Yellow")
print(rc.get_color())
# rc.set_borderwidth("500")
print(rc.get_borderwidth())
