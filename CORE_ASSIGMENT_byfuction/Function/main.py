# def nameage(name, age):
#     print(name, age)


# nameage("Hariom", 26)

# def func1(*args):
#     for i in args:
#         print(i)


# func1(20, 30, 40)
# func1(20, 30)

# def calculation(a, b):
#     return (a+b, a-b)


# res = calculation(40, 10)
# print(res)

# def addition(*numbers):
#     total = 0
#     for i in numbers:
#         total = total+i
#     print("Sum is", total)


# addition()
# addition(10, 5, 54, 23, 2)
# addition(20, 10)

import math
from time import sleep


def factorial(no):
    if no == 0:
        return 1
    else:
        return no*factorial(no-1)


print(factorial(5))

# def selfemployee(name, salary=9000):
#     print("name", name, "Salary", salary)


# selfemployee("Hari", 1200000)
# selfemployee("Jerry")

# def outer_fun(a, b):
#     square = a**2

#     def addition(a, b):
#         return a+b
#     add = addition(a, b)
#     return add+5


# result = outer_fun(5, 15)
# print(result)

# def addition(num):
#     if num:
#         return num+addition(num-1)
#     else:
#         return 0


# res = addition(10)
# print(res)

# def maxnum(a, b, c):
#     print(max(a, b, c))


# (maxnum(22, 1040, 5))

# def sumas(numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total


# print(sumas((8, 2, 3, 10, 7)))

# def mult(numbers):
#     total = 1
#     for i in numbers:
#         total *= i
#     return total


# print(mult((8, 2, 3, -1, 7)))

# def rivrs(list):
#     list1 = list[::-1]
#     return list1


# print(rivrs(('1234abcd')))

# def rivrs(list):
#     revr1 = ''
#     index = len(list)
#     while index > 0:
#         revr1 += list[index-1]
#         index = index-1
#     return revr1


# print(rivrs(('1234abcd')))

# def factl(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factl(n-1)


# n = int(input("Enter a Number"))
# print(factl(n))

# def checknum(n):
#     if n in range(3, 9):
#         print("%s  is in the range" % str(n))
#     else:
#         print("The number is not in range")


# (checknum(18))

# def checklatter(str1):
#     a = 0
#     b = 0
#     for latter in str1:
#         if latter.isupper():
#             a += 1
#         elif latter.islower():
#             b += 1
#         else:
#             pass
#     print("Upper case is ", a)
#     print("Lower case is ", b)


# checklatter("HariomPatidar")

# def newList(list1):
#     list2 = []
#     for chr in list1:
#         if chr not in list2:
#             list2.append(chr)
#     return list2


# print(newList((1, 2, 3, 3, 3, 3, 4, 5)))

# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True


# n = int(input("Enter a Number"))
# print(prime(n))

# def evennum(n):
#     newlist = []
#     for i in n:
#         if i % 2 == 0:
#             newlist.append(i)
#     return newlist


# print(evennum((1, 2, 3, 4, 5, 6, 7, 8, 9)))

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()

# def perfctnum(num):
#     sum = 0
#     for digit in range(1, num):
#         if num % digit == 0:
#             sum += digit
#     return sum == num


# num = int(input("Enter a Number"))
# print(perfctnum(num))

# def tringle(n):
#     raw = [1]
#     y = [0]
#     for i in range(max(n, 0)):
#         print(raw)
#         raw = [l+r for l, r in zip(raw+y, y+raw)]
#     return n >= 1


# print(tringle(6))


# def tamp(cel):
#     fah = cel*9/5+32
#     return fah


# print(tamp(60))


# def tamp(cel):
#     fah = cel*9/5+32
#     return fah


# print(tamp(cel=60))


# def avg(*n):
#     sum = 0
#     for digit in n:
#         sum += digit
#     avg = sum/len(n)
#     return avg


# print(avg(5, 25, 36, 45, 2))


# def tamp(cel):
#     fah = cel*9/5+32
#     return fah


# print(tamp(cel=60))

# import string
# import sys


# def ispenildrom(str1, alphabates=string.ascii_lowercase):
#     alphaset = set(alphabates)
#     return alphaset <= set(str1.lower())


# print(ispenildrom('The quick brown fox jumps over the lazy dog'))

# item = [n for n in input().split("-")]
# item.sort()
# print("-".join(item))

# def printvalue():
#     l = list()
#     for i in range(1, 21):
#         l.append(i**2)
#     print(l)


# printvalue()

# def test(a):
#     def add(b):
#         nonlocal a
#         a += 1
#         return a+b
#     return add


# func = test(4)
# print(func(4))

# my_code = 'print("Heloo World")'
# code = '''
# def multiply(x,y):
#     return x*y
# print("Multiply of x and y is:",multiply(3,6))
# '''
# exec(my_code)
# exec(code)

# def abc():
#     x = 1
#     y = 6
#     z = 58
#     a = "fjnkdnkjrn"
#     b = (2, 5, 2, 5, 2, 55)
#     print("GDFGDFGd")


# print(abc.__code__.co_nlocals)


# def abc(fn, ms, *args):
#     sleep(ms/1000)
#     return fn(*args)


# print("Square root after specific miliseconds:")
# print(delay(lambda x: math.sqrt(x), 100, 16))
# print(delay(lambda x: math.sqrt(x), 1000, 100))
# print(delay(lambda x: math.sqrt(x), 2000, 25100))

# def text(a):
#     def add(b):
#         nonlocal a
#         a += 1
#         return a+b
#     return add


# func = text(4)
# print(func(4))

# def result(a, b):
#     sum = a+b
#     sub = a-b
#     div = a-b
#     mul = a*b
#     print(f"Sum is {sum}\nSub is{sub}\nDiv is{div}\nMul is {mul}")


# a = int(input("Enter a Number"))
# b = int(input("Enter b Number"))
# result(a, b)

# def result(n):
#     lsit1 = [2, 25, 23, 54, 58, 56, 54, 21, 22, 5, 455, 2, 5, 1, 25, 2, 2, 512]
#     if n in lsit1:
#         print("Present")
#     else:
#         print("Absent")


# n = int(input("Enter Your Roll No.\n"))
# result(n)

# def maxnum(a, b, c):
#     return print(max(a, b, c))


# a = int(input("Enter 1 No"))
# b = int(input("Enter 2 No"))
# c = int(input("Enter 3 No"))
# maxnum(a, b, c)

# def oddeven(n):
#     if n % 2 == 0:
#         print("Odd")
#     else:
#         print("Even")


# n = int(input("Enter A Number"))
# oddeven(n)

# def findvovel(n):
#     vov = 0
#     con = 0
#     for i in range(len(n)):
#         if n[i] in ['a', 'e', 'i', 'o', 'u']:
#             vov += 1
#         else:
#             con += 1

#     print("Vovel is\n", vov)
#     print("Consonent is\n", con)


# n = input("Enter a Word\n")
# findvovel(n)

# def chngcase(n):
#     text = n.upper()
#     print(text)


# n = input("Enter a Lowercase Word")
# chngcase(n)

# def area(r):
#     A = 3.14*r**2
#     print("Area of The Circle is: ", A)


# r = int(input("Enter radious of a circle\n"))
# area(r)

# import datetime
# print(datetime.datetime.now())

# def table(n):
#     for i in range(1, 11):
#         t = n*i
#         print("Table is: ", t)


# n = int(input("Enter a Number\n"))
# table(n)


# def factorial(no):
#     factorial = 1
#     if no == 0 or no == 1:
#         print("1")
#     else:
#         for i in range(no, 0, -1):
#             factorial = factorial*i
#     return factorial


# print(factorial(5))

# def fabon(n):
#     count = 0
#     n1 = 0
#     n2 = 1
#     if n == 0 or n == 1:
#         print(n1)
#     else:
#         while count > n:
#             print(n1)
#             n = n1+n2
#             n1 = n2
#             n2 = n
#             count += 1
#             print(count)
#     return


# fabon(8)

