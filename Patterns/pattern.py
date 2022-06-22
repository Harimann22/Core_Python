
a = [2, 4, 6]
b = [2, 4, 6]
for i in a:
    for j in b:
        if j == i:
            continue
        print(i, "*", j, "=", i*j)

# print("----------------------------------------------------------------------->")


for i in range(5):
    for j in range(3):
        print("*", end=" ")
    print(' ')

# print("----------------------------------------------------------------------->")


k = 1
for i in range(8):
    for j in range(0, k):
        print("*", end=" ")
    k += 2
    print(' ')

# print("----------------------------------------------------------------------->")

num = int(input("Enter Your Number\n "))
for i in range(num):
    for j in range(1, i+1):
        print("*", end=" ")
    print(' ')
for i in range(num, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print(' ')

# print("----------------------------------------------------------------------->")

val = 65
for i in range(0, 6):
    for j in range(0, i+1):
        ch = chr(val)
        print(ch, end=" ")
        val = val+1
    print(" ")

# print("----------------------------------------------------------------------->")

k = 1
for i in range(8):
    for j in range(0, k):
        print("*", end=" ")
    k += 2
    print(' ')

# print("----------------------------------------------------------------------->")

n = int(input("Enter Your Number:\n"))
for i in range(n):
    for j in range(i):
        print("*", end=" ")
    print(' ')
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print(' ')

# print("----------------------------------------------------------------------->")

for i in range(1, 11):
    for j in range(1, 11):
        if i > 5 and j > 5:
            break
        print(i*j, end=" ")
    print(" ")

# print("----------------------------------------------------------------------->")

for i in range(1, 11):
    if i > 5:
        break
    for j in range(1, 11):
        print(i*j, end=" ")
    print("")

# print("----------------------------------------------------------------------->")
