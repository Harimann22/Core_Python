list1 = [19,  15, 19, 66, 5, 3, 9, 1, 2]
a = 0
for i in range(0, list1.__len__()-2):

    if list1[i] == list1[i+1]:
        a += 1


if a > 0:
    print("true")
else:
    print("-1")
