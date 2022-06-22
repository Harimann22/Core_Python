from shap import Shape


class Circle(Shape):

    def __init__(self, radious):
        self.radious = radious

    def area(self):
        PI = 3.14
        print(f"Area={PI*self.radious**2}")

    def get_radious(self):
        return self.radious

    def set_radious(self, radious):
        self.radious = radious
