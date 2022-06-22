class Automobile:
    def __init__(self, color, speed, make):
        self.color = color
        self.__speed = speed
        self.__make = make

    def __str__(self):
        return "Color= {} Speed= {} Make= {}".format(self.color, self.__speed, self.__make)

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_make(self):
        return self.__make

    def set_make(self, __make):
        self.__make = __make

    def brek(self, speed):
        if speed < 500:
            print("Good Speed")
        elif speed < 800:
            print("Dont Horry!!!Go Slow....")
        elif speed < 1000:
            print("Warning Go Slow !!!!")
        elif speed >= 1000:
            print("Break!!!You are Going Over Speed")
        else:
            pass

    def get_speed(self, distance, time):
        speed = distance/time
        print("Your Speed is {} km/h".format(speed))

    def gear(self, gear):
        if gear == 1:
            print("Your Speed is 0-300 ")
        elif gear == 2:
            print("Your Speed is 300-500")
        elif gear == 3:
            print("Your Speed is 600-700")
        elif gear == 4:
            print("Your Speed is 700-850")
        elif gear == 5:
            print("Your Speed is 850-1000")
        else:
            print("Please enter Valid Gear")
