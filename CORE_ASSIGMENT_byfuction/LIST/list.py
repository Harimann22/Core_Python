
start = 1
n = 12
k = 2
for i in range(1, n+1, 2):
    gap = k
    if i < 2:
        print(start,  end="")
    else:
        print(f"+ 1/{i}", end=" ")

# print(---------------------------------------------------------------->)

list1 = arr.array('i', [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
find = int(input("Enter a number To find the Position of That: "))
if find in list1:
    print(list1.index(find))
else:
    print("-1")

# print(---------------------------------------------------------------->)

a = [25, 56, 47, 85]
b = [25, 56, 47]

for ele in a:
    if ele in b:
        pass
else:
    print("Missing character is:", ele)

# print(---------------------------------------------------------------->)

a = 20 << 2
print(a)

a = 100 << 5
print(a)

a = 60 >> 3
print(a)

# print(---------------------------------------------------------------->)

num = int(input("Enter the elements number of a list:"))
list1 = []
for ele in range(1, num+1):
    ele = int(input("Enter Elements: "))
    list1.append(ele)
print("The Largest Number In the List is:", max(list1))

# print(---------------------------------------------------------------->)

list1 = [2, 7, 5, 64, 14]
even = [num for num in list1 if num % 2 == 0]
odd = [num for num in list1 if num % 2 != 0]
sumeven = 0
sumodd = 0
for i in even:
    sumeven += i
for i in odd:
    sumodd += i
print("Avrage of all Even numbers is :", sumeven/len(even))
print("Avrage of all Even numbers is :", sumodd/len(odd))

# print(---------------------------------------------------------------->)

list1 = [2, 7, 5, 64, 14]
num = 0
while(num < len(list1)):
    if list1[num] % 2 == 0:
        print(list1[num], end=" ")
    num += 1

# print(---------------------------------------------------------------->)

list1 = [2, 7, 5, 64, 14]
even = 0
for num in list1:
    if num % 2 == 0:
        print("Even", num)

# print(---------------------------------------------------------------->)

list1 = [10, 20, 14, 54, 1115, 48, 165]


def secndmax(list1):
    subline = [x for x in list1 if x < max(list1)]
    return max(subline)


print(secndmax(list1))

# print(---------------------------------------------------------------->)

list1 = [10, 20, 14, 54, 1115, 48, 165]
list1.sort()
print(list1[-2])

# print(---------------------------------------------------------------->)


def my_max(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max


list1 = [10, 20, 14, 54, 1115, 48, 165]
print(my_max(list1))

# print(---------------------------------------------------------------->)

list1 = [10, 20, 14, 54, 1115, 48, 165]
a = list1.sort()
print(list1[-1])
print(max(list1))

# print(---------------------------------------------------------------->)

num = int(input("Enter The Number Of Elemnets in the list:"))
list2 = []
for i in range(1, num+1):
    ele = int(input("Enter Element in the list"))
    list2.append(ele)
print(min(list2))

# print(---------------------------------------------------------------->)

list1 = [10, 20, 14, 54, 5, 48, 165]
list1.sort()
print(list1[0])
print(min(list1))

# print(---------------------------------------------------------------->)

list1 = [2, 4, 6, 8, 5]
first = reduce(lambda x, y: x*y, list1)
print(first)

# print(---------------------------------------------------------------->)

list1 = [2, 4, 6, 8, 5]
a = math.prod(list1)
print(a)

# print(---------------------------------------------------------------->)

list1 = [2, 4, 6, 8, 5]
count = 1
for x in list1:
    count *= x
print(count)

# print(---------------------------------------------------------------->)

list1 = [45, 25, 66, 87, 89, 63, 54]
res = []
for ele in list1:
    sums = 0
    for digit in str(ele):
        sums += int(digit)
    res.append(sums)
print(res)

# print(---------------------------------------------------------------->)

list1 = [2, 25, 45, 63, 54, 21, 2, 3, 6, 5, 47]
count = 0
for i in list1:
    count += i
print(count)

# print(---------------------------------------------------------------->)

list1 = [2, 25, 45, 63, 54, 21, 2, 3, 6, 5, 47]
sums = sum(list1)
avg = sums/len(list1)
print(sums)
print(avg)

# print(---------------------------------------------------------------->)

list1 = [2, 25, 45, 63, 54, 21, 2, 3, 6, 5, 47]
num = int(input("Enter a Number"))
a = list1.count(num)
print(a)
x = 2
d = Counter(list1)
print(d[x])

# print(---------------------------------------------------------------->)

list1 = [1, 2, 3, 4, 5, 5, 5]
list1.clear()
print(list1)
list1 *= 0
print(list1)
del list1[2:5]
print(list1)
list2 = list1[:]
list2 = []
list2.extend(list1)
print(list1, list2)

# print(---------------------------------------------------------------->)

list1 = [1, 2, 3, 4, 5, 5, 5]
exist = list1.count(5)
if exist > 0:
    print("Yes", exist)
else:
    print("No")

# print(---------------------------------------------------------------->)

list1 = [1, 2, 3, 4, 5]
if (4 in list1):
    print("Yes")
else:
    print("No")

# print(---------------------------------------------------------------->)

list1 = [1, 2, 3, 4, 5]
print(length_hint(list1))


a = -451
b = -75
print(max(a, b))

print(a if a >= b else b)

print(a if a < b else b)

# print(---------------------------------------------------------------->)

list1 = [1, 2, 3, 4, 5]
count = 0
for i in list1:
    count += 1
print(count)

# print(---------------------------------------------------------------->)


def swapup(list, pose1, pose2):
    list[pose1], list[pose2] = list[pose2], list[pose1]
    return list


list1 = [1, 2, 3, 4, 5]
pose1, pose2 = 2, 5
print(swapup(list1, pose1-1, pose2-1))

# print(---------------------------------------------------------------->)

list1 = [52, 87, 54, 85, 56]
size = len(list1)

tamp = list1[0]
list1[0] = list1[size-1]
list1[size-1] = tamp
print(list1)

# print(---------------------------------------------------------------->)
