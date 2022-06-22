from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color, borderwidth):
        self.color = color
        self.borderwidth = borderwidth

    def __str__(self):
        return "Color={}\nBorder Width= {}".format(self.get_color(), self.get_borderwidth())

    def area(self):
        pass

    @abstractmethod
    def paramiter(self):
        pass

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_borderwidth(self):
        return self.borderwidth

    def set_borderwidth(self, borderwidth):
        self.borderwidth = borderwidth
