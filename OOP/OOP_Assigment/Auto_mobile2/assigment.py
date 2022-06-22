class Person:
    def __init__(self, name, dob, adress):
        self.name = name
        self.dob = dob
        self.adress = adress

    def __str__(self):
        return "Name ={},Dob={},Adress={} ".format(self.name, self.dob, self.adress)


pr = Person("Hariom", "22/07/1996", "Inore")
print(pr)
