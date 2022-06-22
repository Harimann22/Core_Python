try:
    from itertools import *
    a = input("Enter User Name=")
    if a.isdigit() and a.isalnum():
        raise Exception("Invalid !!!!Dont use Numeric Value")
except Exception as e:
    print(e)

# print(------------------------------------------------------------------------------>)

try:
    a = input("Enter Your Email Address:-")
    if a.isspace() and a.isalnum() and a.isidentifier():
        print("You Are Ragisterd")
    else:
        raise Exception("Please Enter a Valid Mail Id!!!")
except Exception as e:
    print(e)


# print(------------------------------------------------------------------------------>

n = [2, 3, 4], [1, 2, 3, 4, 5, 6]
a = []
for _ in range(3):
    a.append(n[1:])
    print(a)
for i in product(*a):
    print(i)

# print(------------------------------------------------------------------------------>
