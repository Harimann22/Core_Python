num = int(input("Enter a Number to Check it is Palindrom no. or Not:\n"))
rev = 0
temp = num
while num > 0:
    digit = num % 10
    rev = rev*10+digit
    num = num//10
if rev == temp:
    print("{} is a Polindrom Number !".format(temp))
else:
    print("This is Not a Polindrom Number !")

num = int(input("Enter a number:\n"))
incrmt = 1
finlfac = 1
while incrmt <= num:
    finlfac = finlfac*incrmt
    incrmt += 1
print("{} Factorial is :-".format(num), finlfac)

# print(--------------------------------------------------------------------------------->)

o = 0
e = 0
for i in range(100, 201):
    if (i % 2 != 0):
        o += 1
    else:
        e += 1
print("The Odd Numbers in between 100-200 is:-\n", o)
print("The Even Numbers in between 100-200 is:-\n", e)

# print(--------------------------------------------------------------------------------->)

Even = 0
for i in range(10, 101):
    if i % 2 == 0:
        Even += i
print("Sum of all Even  Numbers In Between 10 To 100 is:-\n", Even)

# print(--------------------------------------------------------------------------------->)

num = 0
for i in range(100, 401):
    if i % 7 == 0:
        num += 1
print("Count of The Numbers in Between 100 To 400 All Numbers Who Divisible By 7 is:-", num)

# print(--------------------------------------------------------------------------------->)
