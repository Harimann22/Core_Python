from vehical import Vehical


class Bus(Vehical):
    def __init__(self, name, max_speed=25, milage=0):
        super().__init__(name, max_speed, milage)


bs = Bus("Volvo", 250, 12)
# print(bs.max_speed)
# print(bs)
# print(bs.capacity(50))

print(isinstance(bs, Vehical))
