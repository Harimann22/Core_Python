class Vehical:
    def __init__(self, name, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage
        self.name = name

    def __str__(self):
        return "Max_speed{}\nMilage={}".format(self.max_speed, self.milage)

    def capacity(self, capacity):
        return "The capacity of the {} bus is {}".format(self.name, capacity)


vc = Vehical("Volvo", 300, 25)
