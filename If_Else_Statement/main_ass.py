def marks():
    sub1 = int(input("Enter Marks in Hindi=\n"))
    sub2 = int(input("Enter Marks in English=\n"))
    sub3 = int(input("Enter Marks in Math=\n"))
    sub4 = int(input("Enter Marks in Science=\n"))

    total_marks = sub1+sub2+sub3+sub4

    if total_marks < 120:
        print("You are Fail !")
    elif total_marks > 120 and total_marks < 160:
        print("You Got Grad C")
    elif total_marks > 160 and total_marks < 200:
        print("You Got Grad B")
    elif total_marks > 200 and total_marks < 280:
        print("You Got Grad A")
    elif total_marks > 280 and total_marks <= 320:
        print("You Got Grad A+")
    elif total_marks > 320 and total_marks <= 400:
        print("You Got Grad A++")
    print(f"You Got {total_marks} Marks Out of 400")

# print(----------------------------------------------------------------------------------->)


def oddeven():
    num = int(input("Enter a Number\n"))
    if num > 20:
        if num % 2 == 0:
            print("The number is Even")
        else:
            print("The Number is Odd")
    else:
        print("Number is Less Than 20")


def checkout():
    num = int(input("Enter a Number To Check its Divided by 7 or Not\n"))
    if num % 7 == 0:
        print("True")
    else:
        print("False")

# print(----------------------------------------------------------------------------------->)
