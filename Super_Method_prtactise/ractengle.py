
from Shap import Shape


class Ractangle(Shap):
    def __init__(self, legnth, width):
        self.length = legnth
        self.width = width

    def paramiter(self):
        area = 2*(length+width)
        print(area)


rc = Ractangle(20, 25)
rc.paramiter()
