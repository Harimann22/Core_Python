import sys
from operator import mod
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), (2, "Tiger"), (3, "Fox"), (4, "Wolf"))

print("Size of the First Tuple is:", str(Tuple1.__sizeof__()), "Bytes")
print("Size of the Second tuple is:,", str(Tuple2.__sizeof__()), "Bytes")
print("Size of the Third tuple is:,", str(Tuple3.__sizeof__()), "Bytes")

# print(------------------------------------------------------------------------------>)

list1 = [1, 2, 5, 6]

res = [(val, pow(val, 3)) for val in list1]
print(res)

# print(------------------------------------------------------------------------------>)

test_list = [5, 6, 7]
test_tup = (9, 10)

test_list += test_tup
print(test_list)

# print(------------------------------------------------------------------------------>)

test_list = [5, 6, 7]
test_tup = (9, 10)

res = tuple(list(test_tup)+test_list)
print(res)

# print(------------------------------------------------------------------------------>)

test_tup = (7, 8, 9, 1, 10, 7)
res = sum(test_tup)
print(res)

# print(------------------------------------------------------------------------------>)

test_tup = ([7, 8], [9, 1], [10, 7])
res = sum(list(map(sum, test_tup)))
print(res)

# print(------------------------------------------------------------------------------>)

test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

res = [ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2)]
print(res)

# print(------------------------------------------------------------------------------>)

test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

res = tuple(map(mod, test_tup1, test_tup2))
print(res)

# print(------------------------------------------------------------------------------>)

test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
add_ele = 4

res = [tuple(i+add_ele for i in sub) for sub in test_list]
print(res)

# print(------------------------------------------------------------------------------>)

test_tup = (1, 5, 7, 8, 10)

res = tuple(i*j for i, j in zip(test_tup, test_tup[1:]))
print(res)

# print(------------------------------------------------------------------------------>)

test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

res = []
for sub in test_list:
    if res and res[0][-1] == sub[1]:
        res[-1].extend(sub[1:])
    else:
        res.append([ele for ele in sub])
res = list(map(tuple, res))
print(res)

# print(------------------------------------------------------------------------------>)

tuple1 = (10, 20, 30, 40, 50)
a = tuple1[::-1]
print(a)

# print(------------------------------------------------------------------------------>)

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
res = tuple1[1][1]
print(res)


tuple1 = (50,)
print(tuple1)

# print(------------------------------------------------------------------------------>)

tuple1 = (10, 20, 30, 40)

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])

# secound option
# print(------------------------------------------------------------------------------>)

a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

# print(------------------------------------------------------------------------------>)

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)

# print(------------------------------------------------------------------------------>)

tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 = tuple1[3:-1]
print(tuple2)

# print(------------------------------------------------------------------------------>)

tuple1 = (11, [22, 33], 44, 55)

tuple1[1][0] = 222
print(tuple1)

# print(------------------------------------------------------------------------------>)

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)

# print(------------------------------------------------------------------------------>)

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

# print(------------------------------------------------------------------------------>)

tuple1 = (45, 45, 45, 45,)


def check(t):
    return all(i == t[0] for i in t)


print(check(tuple1))

# print(------------------------------------------------------------------------------>)

tuple1 = (10, 20, 30, 40, 50)
a = tuple1[::-1]
print(a)

# print(------------------------------------------------------------------------------>)

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
a = tuple1[1][1]
print(a)

# print(------------------------------------------------------------------------------>)

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2, tuple1

print(tuple1)
print(tuple2)

# print(------------------------------------------------------------------------------>)

tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 = tuple1[3:-1]
print(tuple2)

# print(------------------------------------------------------------------------------>)

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

# print(------------------------------------------------------------------------------>)

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
a = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(a)

# print(------------------------------------------------------------------------------>)

tuple1 = (50, 10, 60, 70, 50, 50)

count = 0
for i in tuple1:
    if i == 50:
        count += 1
print(count)

# print(------------------------------------------------------------------------------>)

tuple1 = (45, 45, 45, 45, )


def check(t):
    return all(i == t[1] for i in t)


print(check(tuple1))

tup = [('for', 2), ('is', 9), ('to', 7), ('Go', 5), ('or', 15), ('a', 13)]

a = [tuple(sorted(list(tup), key=lambda x:x[0]))]
print(a)

# print(------------------------------------------------------------------------------>)

res = input("Enter the comma seprated numbers:")
list1 = res.split(",")
tup = tuple(list1)
print("List:", list1)
print("Tuple:", tup)

# print(------------------------------------------------------------------------------>)

test_tup = (7, 5, 9, 1, 10, 3)
res = sum(list(test_tup))
print(res)

# print(------------------------------------------------------------------------------>)
