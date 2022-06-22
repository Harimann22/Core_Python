
import datetime


def pattern1(raw):
    raw = int(input("Enter a Number"))
    for i in range(1, raw+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()
#     print("------------------------------------")


ch = 65
for i in range(1, 6):
    for j in range(1, i+1):
        alfa = chr(ch)
        print(alfa, end=" ")
        ch += 1
    print()

# print("----------------------------------------------")

ch = 65
for i in range(1, 6):
    for j in range(1, i+1):
        alfa = chr(ch)
        ch += 1
        print(alfa, end=" ")
    ch = 65
    print()

print("--------------------------------------------------")

a = datetime.datetime.now()
b = datetime.datetime(1996, 7, 22)
age = a.year
age2 = b.year
print(age-age2)


def area_cir(pai, r):
    A = pai*r**2
    return A
