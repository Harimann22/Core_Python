class vehicale:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage


modellX = vehicale(240, 18)
print(modellX.max_speed, modellX.milage)

# print(----------------------------------------------------------------------------------------------------------->)


class vehicale:
    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

    def seeting_capacity(self, capacity):
        return f"The seeting Capacity of the {self.name} is {capacity} Passanger"

# print(----------------------------------------------------------------------------------------------------------->)


class Bus(vehicale):
    def seeting_capacity(self, capacity=50):
        return super().seeting_capacity(capacity=50)


school_bus = Bus("Volvo Bus", 254, 24)
print("Vehicle Name", school_bus.name, "Max_Speed ",
      school_bus.max_speed, "Milage of Bus is ", school_bus.milage, school_bus.seeting_capacity())

# print(----------------------------------------------------------------------------------------------------------->)


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass

# print(----------------------------------------------------------------------------------------------------------->)
