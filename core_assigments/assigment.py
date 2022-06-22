import random

a = 251
b = 75
if a > b:
    print("a is Grater than b")
else:
    print("b is greater Than a")

# print(----------------------------------------------------------------------------------->)

for i in range(5):
    a = random.randrange(1, 100)
    print(a)

# print(----------------------------------------------------------------------------------->)

num = int(input("Enter Your number find fect:"))
c = 1
for i in range(1, num+1):
    c = c * i
print(c)

# print(----------------------------------------------------------------------------------->)

list1 = [1, 2, 55, 44, 52, 54, 56]
list2 = list(reversed(list1))
print(list2)

# print(----------------------------------------------------------------------------------->)

nterm = int(input("Enter Your Number"))
n1, n2 = 0, 1
count = 0

if nterm < 0:
    print("Please Enter a Positive Number:")
elif nterm == 1:
    print(n1)
else:
    while count < nterm:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1

# print(----------------------------------------------------------------------------------->)

count = 0
for i in range(100, 200):
    if (i % 7 == 0):
        print(i)
        count = count+i
print(count)

# print(----------------------------------------------------------------------------------->)

rows = 9
column = 10

for i in range(2, column+1):
    for j in range(1, rows+2):
        final = j*i
        print(format(final), end=" ")
    print("\n")

# print(----------------------------------------------------------------------------------->)

for i in range(1, 5):
    print(f"{i}"*i)

# print(----------------------------------------------------------------------------------->)

num = int(input("Enetr Your Number:"))
sum = 0
tamp = num
while tamp > 0:
    digit = tamp % 10
    sum += digit**3
    tamp //= 10

if num == sum:
    print("Yes It is a Armstrong Number")
else:
    print("No It is Not a  Armstrong Number")

# print(----------------------------------------------------------------------------------->)

num = int(input("Enter a number"))

if (num > 1):
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print("The number is Not a Prime Number:")
            break
    else:
        print("The number is a Prime Number:")
else:
    print("The number is Not a Prime Number:")

# print(----------------------------------------------------------------------------------->)

num = int(input("Enter a Number:"))
rev = 0

term = num
while num > 0:
    digit = num % 10
    rev = rev*10+digit
    num = num//10
if term == rev:
    print("This is a Polindrom Number")
else:
    print("This is Not a Polindrom Number")

# print(----------------------------------------------------------------------------------->)

firtrm = 1
dif = 5
nthterm = 8
i = 1
j = 0
print("1+")
while(i < 5):
    j += 1/i
    print("1/", i, "+")
    i += 1
# print(j)

# print(----------------------------------------------------------------------------------->)

first = int(input("Enter first number:"))
secnd = int(input("Enter secund no:"))

userinput = int(input(
    "Press 1. To Add.\nPress 2. To Sub\nPress 3. To Mul\nPress 4. To Div"))

if userinput == 1:
    sum = first+secnd
    print(sum)
elif userinput == 2:
    Sub = first-secnd
    print(Sub)
elif userinput == 3:
    Mul = first*secnd
    print(Mul)
elif userinput == 4:
    Div = first/secnd
    print(Div)
else:
    print("Please Choose the Right Unit")

# print(----------------------------------------------------------------------------------->)
