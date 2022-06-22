a = "HariomPatidar"
for i in a:
    if i == 'P':
        continue
    print(i, end="")

# print("----------------------------------------------------------------------->")

a = "HariomPatidar"
for i in a:
    if i == 'P':
        break
    print(i, end="")

# print("----------------------------------------------------------------------->")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sum = 0
count = 0
for i in numbers:
    sum = sum+i
    count = count+1
    if count == 5:
        break

print(sum)

# print("----------------------------------------------------------------------->")

sum = 0
count = 0
while (count < 10):
    sum = sum+count
    count += 1
    if count == 5:
        break
print(sum)

# print("----------------------------------------------------------------------->")

for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i)

# print("----------------------------------------------------------------------->")

numbers = [10, 40, 120, 230]
for i in numbers:
    if i > 100:
        break
    print(i)

# print("----------------------------------------------------------------------->")

name = "Hariom22 Patidar"
size = len(name)
i = 0
while i < size:
    if name[i].isspace():
        break
    print(name[i], end="")
    i = i+1

# print("----------------------------------------------------------------------->")


numbers = [2, 3, 11, 7]
for i in numbers:
    if i > 10:
        continue
    print("The current Number is:-", i)
    print("Square of Number is:", i*i)

# print("----------------------------------------------------------------------->")

for raw in range(1, 6):
    for col in range(1, raw+1):
        print(raw*col)

for i in range(100):
    if i == 8:
        break
    print(i)

# print("----------------------------------------------------------------------->")
