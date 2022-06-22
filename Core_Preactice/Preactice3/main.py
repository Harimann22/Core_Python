import sys
import collections
list1 = [1, 25, 4, 31, 25, 56]
res = []
a = [x for x in list1 if x % 2 != 0]
res.append(a)
print(a)

# print(------------------------------------------------------------------------------>)

i = 0
while i < len(list1):
    if list1[i] % 2 != 0:
        print(list1[i], end=" ")
    i += 1

odd = list(filter(lambda x: (x % 2 != 0), list1))
print(odd)

# print(------------------------------------------------------------------------------>)

start = int(input("Enter Start Number: "))
end = int(input("Enter End Number: "))
for i in range(start, end+1):
    if i % 2 == 0:
        print(i)

# print(------------------------------------------------------------------------------>)

start = int(input("Enter Start Number: "))
end = int(input("Enter End Number: "))
for i in range(start, end+1, 2):
    print(i)

# print(------------------------------------------------------------------------------>)

list1 = [2, 7, 5, 64, 14, 5, 9, 7]
odd = [x for x in list1 if x % 2 != 0]
even = [y for y in list1 if y % 2 == 0]
print(len(odd))
print(len(even))

# print(------------------------------------------------------------------------------>)

list1 = [2, 7, 5, 64, 14, 5, 9, 7, 2]
odd, even = 0, 0
x = 0
while x < len(list1):
    if x % 2 != 0:
        odd += 1
    else:
        even += 1
    x += 1
print(odd)
print(even)

# print(------------------------------------------------------------------------------>)

list1 = [2, 7, 5, 64, 14, 5, 9, 7, 2]
odd = len(list(filter(lambda x: (x % 2 != 0), list1)))
even = len(list(filter(lambda x: (x % 2 == 0), list1)))
print(odd)
print(even)

# print(------------------------------------------------------------------------------>)

list1 = [12, -7, 5, 64, -14]
poss = list(filter(lambda x: x > 0, list1))
poss1 = list(filter(lambda x: x < 0, list1))
print(poss)
print(poss1)

# print(------------------------------------------------------------------------------>)

start = int(input("Enter Start Number: "))
end = int(input("Enter End Number: "))
for i in range(start, end+1):
    if i >= 0:
        print(i)

# print(------------------------------------------------------------------------------>)

str1 = " geeks quiz practice code"
str2 = str1.split()[::-1]
l = []
for i in str2:
    l.append(str2)
print(str2)

# print(------------------------------------------------------------------------------>)

str1 = " geeks quiz practice code"
print(len(str1))

counter = 0
for i in str1:
    counter += 1
print(counter)

# print(------------------------------------------------------------------------------>)

a = [2, 5, 3, 8]
b = [2, 5, 3]

for i in a:
    if i not in b:
        print(i)


a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# print(------------------------------------------------------------------------------>)

for i in a:
    find = int(input("Enter a Number to find : "))
    if find in a:
        print(a.index(find))
    else:
        print("-1")

country_code = {'India': '0091',
                'Australia': '0025',
                'Nepal': '00977'}
# print(country_code.get('India', 'Not Found'))
# print(country_code.get('Japan', 'Not Found'))
country_code.setdefault('Japan', 'Not In List')
print(country_code['India'])
print(country_code['Japan'])

# print(------------------------------------------------------------------------------>)

dic = collections.defaultdict(lambda: 'Key Not Found')
dic['a'] = 'Hari'
dic['b'] = 'Patidar'
print(dic['a'])
print(dic['j'])
print(dic['h'])

dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}
print(sys.getsizeof(dic1), "+bytes")
print(sys.getsizeof(dic2), "+bytes")
print(sys.getsizeof(dic3), "+bytes")

print(dic1.__sizeof__(), "+bytes")

# print(------------------------------------------------------------------------------>)

a = []
for num in range(100, 200):
    a.append(num)
    for j in a:
        digit = a//10
        print(a)
# print(------------------------------------------------------------------------------>)

test_set = set("geEks")
for vel in test_set:
    print(vel)

# print(------------------------------------------------------------------------------>)

set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
print(min(set))

# print(------------------------------------------------------------------------------>)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
p = 0
for i in a:
    if i in b:
        p += 1
if(p > 0):
    print("True")
else:
    print("false")

# print(------------------------------------------------------------------------------>)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 5]
result = 0
for x in a:
    for y in b:
        if x == y:
            result += 1
        else:
            result = 0
if result > 0:
    print("True")
else:
    print("False")

# print(------------------------------------------------------------------------------>)
