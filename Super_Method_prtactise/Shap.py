class Shape:
    def __init__(self, color, border_width):
        self.color = color
        self.border_width = border_width

    def __str__(self):
        return "Color ={}\nBorder Width = {}".format(self.color, self.border_width)

    def get_color(self):
        return self.color

    def set_color(self):
        self.color = color

    def get_border_width(self):
        return self.border_width

    def set_border_width(self, border_width):
        self.border_width = border_width

    def paramiter(self):
        return -1
