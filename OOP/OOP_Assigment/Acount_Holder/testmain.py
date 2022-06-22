import main
from main import *
pr = Person()
pr.set_name("Hariom Patidar")
pr.set_Address("Indore")
pr.set_DOB("22/07/1996")

print(pr.get_name())
print(pr.get_Address())
print(pr.get_DOB())

print(Person().age)
