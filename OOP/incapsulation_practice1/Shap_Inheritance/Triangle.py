from shap import Shape


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(self.height*self.base/2)

    def get_base(self):
        return self.base

    def set_base(self, base):
        self.base = base
