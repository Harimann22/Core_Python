import random


def maxim(a, b):
    if a > b:
        print("A is Greater than B")
    else:
        print("B is Greater than A")

# print(------------------------------------------------------------------------------->)


def randm(n):
    for i in range(n):
        a = random.randrange(1, 100)
        print(a, end=" ")

# print(------------------------------------------------------------------------------->)


def factorial(n):
    sum = 1
    for i in range(n, 0, -1):
        sum = sum*i
    print(sum)

# print(------------------------------------------------------------------------------->)


def rev(n):
    revrse = 0
    while n != 0:
        digit = n % 10
        revrse = revrse*10+digit
        n //= 10
    print(revrse)

# print(------------------------------------------------------------------------------->)


def fibonachhi(n):
    n1 = 0
    n2 = 1
    count = 0
    if n < 0:
        print("Please Enter a Positive Number")
    elif n == 1:
        print(n1)
    else:
        while count < n:
            print(n1)
            nth = n1+n2
            n1 = n2
            n2 = nth
            count += 1

# print(------------------------------------------------------------------------------->)


def divisibl():
    sum = 0
    count = 0
    for i in range(100, 201):
        if i % 7 == 0:
            sum += i
            count += 1
    avg = sum/count
    print(avg)

# print(------------------------------------------------------------------------------->)


def table(raw, col):
    for i in range(2, 11):
        for j in range(1, 11):
            print(i*j, end=" ")
        print()

# print(------------------------------------------------------------------------------->)


def tringle(n):
    for i in range(1, n):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# print(------------------------------------------------------------------------------->)


def armstrong(num):
    sum = 0
    tamp = num
    while tamp > 0:
        digit = tamp % 10
        sum += digit**3
        tamp //= 10
    if num == sum:
        print("Yes Given Number is Armstrong Number")
    else:
        print("No Given Number is Not Armstrong Number")

# print(------------------------------------------------------------------------------->)


def prime(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    if count > 0:
        print("No it is Not a Prime Number")
    else:
        print("Yes it is a Prime Number")

# print(------------------------------------------------------------------------------->)


def polindrom(num):
    rev = 0
    term = num
    while num > 0:
        digit = num % 10
        rev = rev*10+digit
        num //= 10
    if term == rev:
        print("Yes this is a Polindrom Number")
    else:
        print("No this is Not a Polindrom Number")

# print(------------------------------------------------------------------------------->)


def avrge(num):
    oddsum = 0
    evensum = 0
    oddcount = 0
    evencount = 0
    for i in range(1, num+1):
        if i % 2 == 0:
            oddsum += i
            oddcount += 1
        if i % 2 != 0:
            evensum += i
            evencount += 1
    oddavg = oddsum/oddcount
    evenavg = evensum/evencount
    print("Odd no Avrage is ", oddavg)
    print("Even no Avrage is ", evenavg)

# print(------------------------------------------------------------------------------->)


def short(*list1):
    new_list = set(list1)
    new_list.remove(max(new_list))
    print(max(new_list))

# print(------------------------------------------------------------------------------->)


def findele():
    a = [22, 44, 55, 66]
    b = [22, 44, 55]
    for i in a:
        if i in b:
            pass
        else:
            print(i)


findele()

# print(------------------------------------------------------------------------------->)


def findlnum():
    list1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    find = int(input("Enetr a Number to Find Index of it"))
    if find in list1:
        print(list1.index(find))
    else:
        print("-1")

# print(------------------------------------------------------------------------------->)
