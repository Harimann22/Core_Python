from shap import Shape


class Ractangal(Shape):
    def __init__(self, length, width, col, bw):
        super().__init__(col, bw)
        self.length = length
        self.width = width

    def sume(self, a, b):
        sume = a+b
        print(sume)

    def area(self):
        area = self.length*self.width
        print(area)

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def paramiter(self):
        pera = 2*(self.length*self.width)
        print(pera)
