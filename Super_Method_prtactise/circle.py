
from Shap import Shape


class Circle(Shape):

    def __init__(self, radious, color, border_width):
        super().__init__(color, border_width)
        self.radious = radious

    def paramiter(self):
        PI = 3.14
        pera = 2*PI*self.radious
        print(pera)


cr = Circle(4, " Red", 2)
cr.paramiter()
