class Shape:
    def __init__(self, color, borderwidth):
        self.color = color
        self.borderwidth = borderwidth

    def __str__(self):
        return f"Color={self.color}\nBorder Width = {self.borderwidth}"

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_borderwidth(self):
        return self.borderwidth

    def set_borderwidth(self, borderwidth):
        self.borderwidth = borderwidth
