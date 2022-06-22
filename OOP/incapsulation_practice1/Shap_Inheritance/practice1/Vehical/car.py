from vehical import Vehical


class Car(Vehical):
    def __init__(self, name, max_speed, milage):
        super().__init__(name, max_speed, milage)


cr = Car("Baleno", 600, 18)
print(cr.name)
print(cr.max_speed)
print(cr.milage)
print(cr.capacity(4))
