from shap import Shape


class Ractangle(Shape):
    def __init__(self, color, bw, length, width):
        super().__init__(color, bw)
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

    def sum(self):
        return -1

    def mass(self):
        return self.length+self.width
