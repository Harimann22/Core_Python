
list1 = [11, 12, 14, 13, 14, 13, 15, 14]
if len(list1) == 8:
    if list1[5] >= 3:
        print("True")
    else:
        print("False")
else:
    print("False")

# print(--------------------------------------------------------------------------------->)


def Check(num):
    if num % 34 == 4 and num > 4**4:
        print("True")
    else:
        print("False")


Check(854)

# print(--------------------------------------------------------------------------------->)


def pile_stone(num):
    if num % 2 == 0:
        for i in range(num, ):
            print(num+2*i)
    if num % 2 != 0:
        for j in range(num,):
            print(num+2*j)


pile_stone(11)

# print(--------------------------------------------------------------------------------->)


def checkstring(list1):
    if list1[len(list1)-2] in list1[len(list1)-1]:
        print("True")
    elif list1[len(list1)-2] != list1[len(list1)-1]:
        print("False")


checkstring(['a', 'abb', 'sfs', 'oo', 'de', 'sfde'])

# print(--------------------------------------------------------------------------------->)


def check(list1):
    return all(i in range(1000) and abs(i-j) >= 10 for i in list1 for j in list1 if i != j) and len(list1) == 100


nums = list(range(0, 1000, 10))
print(nums)
print(check(nums))
nums = list(range(0, 1000, 20))
print(nums)
print(check(nums))

# print(--------------------------------------------------------------------------------->)

list1 = [2, 2, 2, 2, 2]
sums = 0
for i in list1:
    sums += i
if list1.count(i) == sums:
    print("True")
else:
    print("False")

str1 = "The dance, held in the school gym, ended at midnight."
print(str1.split(" "))

# print(--------------------------------------------------------------------------------->)


def check(nums):
    return [nums[i] != nums[i+1] for i in range(len(nums)-1)] and len(set(nums)) == 4


nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(check(nums))
nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(check(nums))

# print(--------------------------------------------------------------------------------->)


def combination(test1):
    ls = []
    s = ""
    for i in test1.replace(' ', ''):
        s += i
        if s.count('(') == s.count(')'):
            ls.append(s)
            s = ''
    return ls


test1 = '(())((()()()))(())()'
print(combination(test1))

# print(--------------------------------------------------------------------------------->)


def check(nums, n):
    return [i for i, n in enumerate(nums) if n < thress]


nums = (0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55)
thress = 100
print(check(nums, thress))

# print(--------------------------------------------------------------------------------->)


def pali(str1):
    return [s == s[::-1] for s in str1]


str1 = ['palindrome', 'madamimadam', '', 'foof', 'eyes']
print(pali(str1))
