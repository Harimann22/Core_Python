
a = [[1, 2], [3, 4]]
m = 1
for i in range(0, 2):
    m *= 10
    for j in range(0, 2):
        a[i][j] *= m
print(a)

# print("----------------------------------------------------------------------->")

a = [['Animal', 'Models', 'Cars'], ['Lion', 'Ironman', 'Brezza']]
for i in a:
    for j in i:
        print(j)

# print("----------------------------------------------------------------------->")

a = ["A", "B", "C", "D"]
for i in a:
    for j in (1,):
        print(i, end=" ")
    print()

# print("----------------------------------------------------------------------->")

a = "Pathon Logic for Kids"
for i in a:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        continue
    print(i, end=" ")

# print("----------------------------------------------------------------------->")

nam = input("Enter Your Name\n")
for i in range(5):
    for j in range(3):
        print(nam, end=" ")
    print(' ')

# print("----------------------------------------------------------------------->")

names = ["Hari", "Sourabh"]
for name in names:
    count = 0
    while count < 5:
        print(name, end=" ")
        count += 1
    print()

# print("----------------------------------------------------------------------->")

for i in range(4):
    for j in range(4):
        if j == i:
            break
        print(i, j)

# print("----------------------------------------------------------------------->")

a = [2, 8, 6]
c = [24, 85, 61]
final = [a+c for i in a for j in c]
print(final)

# print("----------------------------------------------------------------------->")

sum = 1
i = 10
while i > 10:
    num = input("Enter number")
    sum = sum+num
    i = i-1
print(sum/10)

# print("----------------------------------------------------------------------->")

i = 1
while i <= 10:
    print(24*i)
    i = i+1

# print("----------------------------------------------------------------------->")

i = 1
fac = 1
num = int(input("Enetr a Number"))
while i < num:
    fac = fac*num
    num -= 1
print(fac)

# print("----------------------------------------------------------------------->")

x = int(input())
y = int(input())
while y != 0:
    x, y = y, x % y
print(x)


# print("----------------------------------------------------------------------->")

serial = [1, 2, 3]
weekday = ["What", "When", "Why"]
for i in serial:
    print(i)
    for j in weekday:
        print(j)

# print("----------------------------------------------------------------------->")

weather = ["snow", "rain", "sun", "clouds"]
for i in weather:
    if i == 'sun':
        continue
    print(i)

# print("----------------------------------------------------------------------->")
