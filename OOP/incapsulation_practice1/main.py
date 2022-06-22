import builtins
import array
for name in array.__dict__:
    print(name)


class Student:
    def __init__(self, name, student_roll, class_name):
        self.name = name
        self.student_roll = student_roll
        self.class_name = class_name


stdnt = Student("Hariom", "0805CE131029", "Civil")
print(stdnt.__dict__)

print(help(builtins.abs(-155)))


def student(student_id, student_name, student_class):
    return f"Student Name = {student_name}\nStudent Class = {student_class}\nStudent Id = {student_id}"


print(student("58475645", "Hariom", "VI"))


def student_data(student_id, **list1):
    print(f"Student Id =", {student_id})
    if 'student_name' in list1:
        print(f"Student Name = ", {list1['student_name']})
    if 'student_name' and 'student_class' in list1:
        print(f"Student Name= ", {list1['student_name']})
        print(f"Student Class= ", {list1['student_class']})


student_data('I5ADFG', student_name='Hariom')
student_data('I5AHgfG', student_name='Sourbh', student_class='VI')

# print(---------------------------------------------------------------------------->)


class Student:
    pass


print(type(Student))
print(Student.__dict__)
print(Student.__module__)


class Student:
    student_id = 'DSSFDS'
    student_name = 'Hariom'


for ttr, value in Student.__dict__.items():
    if not ttr.startswith('_'):
        print(f"{ttr}-->{value}")
Student().student_class = 'V'
for ttr, value in Student().__dict__.items():
    if not ttr.startswith('_'):
        print(f"{ttr}--->{value}")
del Student.student_name
for ttr, value in Student().__dict__.items():
    if not ttr.startswith('_'):
        print(f"{ttr}--->{value}")

# print(---------------------------------------------------------------------------->)


class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num//val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(4000))

# print(---------------------------------------------------------------------------->)


class py_num:
    def int_roman(self, num):
        val = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4,
               1]
        sys = ["M", "CM", "D", "CD",
               "C", "XC", "L", "XL",
               "X", "IX", "V", "IV",
               "I"]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num//val[i]):
                roman_num += sys[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_num().int_roman(58))

# print(---------------------------------------------------------------------------->)


class py_solution:
    def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
                print(parenthese)
                # print((stack.pop()))
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0


print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))

# print(---------------------------------------------------------------------------->)


class py_solution:
    def check_paranthesis(self, str1):
        store = []
        list1 = {'(': ')', '[': ']', '{': '}'}
        for paranthisis in str1:
            if paranthisis in list1:
                store.append(paranthisis)
            elif store == 0 or list1[store.pop()] != paranthisis:
                return False
        return len(store) == 0


print(py_solution().check_paranthesis("[{([)}]"))

# print(---------------------------------------------------------------------------->)


class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]


print(py_solution().sub_sets([4, 5, 6]))

# print(---------------------------------------------------------------------------->)


class py_solution:
    def two_num(self, num, target):
        dic = {}
        for i, num in enumerate(num):
            if target-num in dic:
                return (dic[target-num], i)
            dic[num] = i


print("Index 1=%d\nIndex 2= %d" %
      py_solution().two_num((10, 44, 88, 40, 25, 65), 50))

# print(---------------------------------------------------------------------------->)


class py_solution:
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result


print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

# print(---------------------------------------------------------------------------->)


class py_solution:
    def pow(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x

        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n == 0:
            return 1
        if n < 0:
            return 1/self.pow(x, -n)
        val = self.pow(x, n//2)
        print(val)
        if n % 2 == 0:
            return val*val
        return val*val*x


print(py_solution().pow(-1, 3))
print(py_solution().pow(3, 5))
print(py_solution().pow(100, 0))

# print(---------------------------------------------------------------------------->)


class py_solution:
    def pow(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x
        if x == -1:
            if n % 2 == 0:
                return -1
            else:
                return -1
        if n == 0:
            return -1
        if n < 0:
            return 1/self.pow(x, -n)
        val = self.pow(x, n//2)
        if n % 2 == 0:
            return val*val
        else:
            return val*val*x


print(py_solution().pow(-1, 3))
print(py_solution().pow(3, 5))
print(py_solution().pow(100, 0))

# print(---------------------------------------------------------------------------->)


class py_solution:
    def revrse(self, s):
        return " ".join(reversed(s.split()))


print(py_solution().revrse("Hariom Patidar"))


class uppoer:
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input()

    def print_string(self):
        print(self.str1.upper())


str1 = uppoer()
str1.get_string()
str1.print_string()

# print(---------------------------------------------------------------------------->)


class Ractangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length*self.width
        print(area)


rc = Ractangle(25, 2)
rc.area()

# print(---------------------------------------------------------------------------->)


def sumes(num):
    sum = 0
    for i in range(0, num+1):
        sum = sum+i
    print(sum)


sumes(5)

# print(---------------------------------------------------------------------------->)
