class Person:
    age = 26

    def __init__(self):
        self.__name = None
        self.__DOB = 0
        self.__Address = None
        self.__age = 0

    def get_name(self):
        return self.name

    def get_DOB(self):
        return self.DOB

    def get_Address(self):
        return self.Address

    def set_name(self, name):
        self.name = name

    def set_DOB(self, DOB):
        self.DOB = DOB

    def set_Address(self, Adress):
        self.Address = Adress
