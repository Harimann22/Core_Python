# '''Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). Go to the editor
# Click me to see the sample solution'''
import random


def findnum(c):
    a = []
    for i in range(1500, 2700):
        if i % 7 == 0:
            i*5
            print(i)
    result = c * 1.8+32
    print(result)

# print(---------------------------------------------------------------------------->)


a = int(input("Choose a Number : Between 1 To 9 \n  "))
comp = random.randrange(1, 10)
print(f"Computer Choose {comp}")
if a == comp:
    print("Congratulations! You Guess Right Answer...")
else:
    print("oops!Its not match Better Luck Next Time..")

# print(---------------------------------------------------------------------------->)

a = input("Enter a Word\n")
print(a[::-1])

datalist = [1452, 11.23, 1+2j, True, 'w3resource',
            (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
datalist
for i in datalist:
    print(i, type(i))

# print(---------------------------------------------------------------------------->)

a = []
for i in range(0, 6):
    a.append(i)
a.remove(3)
print(a)

# print(---------------------------------------------------------------------------->)

for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    print(i)

# print(---------------------------------------------------------------------------->)

a = "Hariom Patidar"
count = 0
for i in a:
    if i == 'a':
        count += 1
print(count)

# print(---------------------------------------------------------------------------->)

raw = 3
colomn = 4
multi = [[0 for i in range(colomn)] for j in range(raw)]
for i in range(raw):
    for j in range(colomn):
        multi[i][j] = i*j
print(multi)

# print(---------------------------------------------------------------------------->)

line = []
while True:
    s = input()
    if s:
        line.append(s.lower())
    else:
        break
for sentance in line:
    print(sentance)

# print(---------------------------------------------------------------------------->)

list1 = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x % 5:
        list1.append(p)
print(",".join(list1))

# print(---------------------------------------------------------------------------->)

digit = 0
charcter = 0
a = "srs6548654dsfsdffsd52"
for i in a:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        charcter += 1
    else:
        pass
print("Digit is:", digit)
print("Character is:", charcter)

# print(---------------------------------------------------------------------------->)

num = int(input("Enter a Number"))
s = 1
while (num > 0):
    s = num * s
    num = num-1
print(s)

# print(---------------------------------------------------------------------------->)

num = int(input("Enter the number"))
rem = 0
nex = 0
while rem <= num:
    nex = nex+rem
    rem += 1
print(nex)

# print(---------------------------------------------------------------------------->)

lst = [10, 99, 98, 85, 45, 59, 65, 100, 66, 76, 12, 35, 13, 100, 80, 95]
index = 0
ele = 0
while index < lst.__len__():
    if lst[index] == 100:
        print(index)
        ele += 1
    index += 1
if ele > 0:
    pass
else:
    print("-1")

# print(---------------------------------------------------------------------------->)
