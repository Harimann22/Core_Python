import assigmnt_pattern as ap
for i in range(6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
# print("-------------------------------------------------------------")
for i in range(6, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()
# print("------------------------------------------------------------------")

k = 8
for i in range(5):
    for j in range(0, k):
        print(end=" ")
    k = k-2
    for j in range(1, i+1):
        print("*", end=" ")
    print()
# print("------------------------------------------------------------------")

k = 16
l = 1
for i in range(0, 5):
    for j in range(0, k):
        print(end=" ")
    k = k-4
    for j in range(0, l):
        print("* ", end="")
    l = l+2
    print()
# print("--------------------------------------------------------------------")

k = 1
for i in range(0, 5):
    for j in range(0, i+1):
        print(k, end=" ")
        k = k+1
    print()
# print("----------------------------------------------------------------------")

for i in range(0, 5):
    n = 1
    for j in range(0, i+1):
        print(n, end=" ")
        n = n+1
    print()

# print("--------------------------------------------------------------------------")

num = 1
inc = 1
for i in range(0, 5):
    for j in range(0, inc):
        print(num, end=" ")
        num = num+1
    print()
    inc = inc+2
# print("-----------------------------------------------------------------------------")

raw = int(input("Enter a Number"))
k = 0
for i in range(1, raw+1):
    for j in range(1, (raw-i)+1):
        print(end=" ")
    while k != (2*i-1):
        print("*", end="")
        k += 1
    k = 0
    print()
# print("-----------------------------------------------------------------------------------")

raw = int(input("Enter a Number"))
k = 0
count = 0
count1 = 0
for i in range(1, raw+1):
    for j in range(1, (raw-i)+1):
        print("  ", end="")
    while k != (2*i-1):
        if count <= raw-1:
            print(i+k, end=" ")
            count += 1
        else:
            count1 += 1
            print((i+k)-2*count1, end=" ")
        k += 1
    count = count1 = k = 0
    print()

# print(-------------------------------------------------------------------------------------------->)

raw = int(input("Enter number of rows: "))
for i in range(raw, 1, -1):
    for space in range(0, raw-i):
        print(" ", end="")
    for j in range(i, 2*i-1):
        print("*", end="")
    for j in range(1, i-1):
        print("*", end="")
    print()

# print(----------------------------------------------------------------------------------------------------------->)

k = 0
for i in range(0, 5):
    for j in range(0, i+1):
        k += 1
        print(k, end=" ")
    print()

# print(----------------------------------------------------------------------------------------------------------->)

k = 0
for i in range(0, 5):
    for j in range(0, i+1):
        k += 1
        print(k, end=" ")
    k = 0
    print()

# print(----------------------------------------------------------------------------------------------------------->)

k = 1
inc = 1
for i in range(0, 5):
    for j in range(0, inc):
        print(k, end=" ")
        k += 1
    print()
    inc = inc+2

# print(----------------------------------------------------------------------------------------------------------->)

k = 0
for i in range(0, 10):
    for j in range(1, i+1):
        print(k, end=" ")
    k += 1
    print()

# print(----------------------------------------------------------------------------------------------------------->)

for i in range(0, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# print(----------------------------------------------------------------------------------------------------------->)

for i in range(1, 8):
    for j in range(-1+i, -1, -1):
        print(format(2**j, "4d"), end=" ")
    print()

# print(----------------------------------------------------------------------------------------------------------->)

ch = 65
inc = 0
for i in range(1, 7):
    for j in range(1, inc):
        alfa = chr(ch)
        ch += 1
        print(alfa, end=" ")
    inc += 2
    print()

# print(----------------------------------------------------------------------------------------------------------->)

decrement = 8
counter = 64
value = 65
for i in range(0, 5):
    for k in range(0, decrement):
        print(end=" ")
    for j in range(0, i+1):
        counter = counter+1
    value = counter
    tamp = value
    for j in range(0, i+1):
        ch = chr(value)
        print(ch, end=" ")
        value = value-1
    value = tamp
    decrement = decrement-2
    print()

# print(----------------------------------------------------------------------------------------------------------->)

a = ap.pattern1(5)
print(a)

a = ap.area_cir(3.14, 14)
print(a)

# print(----------------------------------------------------------------------------------------------------------->)
