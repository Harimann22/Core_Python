import random
import string

def match():
 player = int(input("Enter Your Number beetween 1 to 6:"))
 if player in range(0, 7):
    computer = [1, 2, 3, 4, 5, 6]

    computer = random.choice(computer)
    print("computer Genrate Number:", computer)
    if player == computer:
        print("The match is Tie")

    elif player > computer:

        print("You Won")
    else:
        print("You Loose")


# a = []
# for i in range(5):
#     a.append(random.randint(20, 60))

# print(a)

# a = []
# for i in range(1):
#     a.append(random.randint(0, 9999))
# print(a)


# posi = string.ascii_letters+string.digits
# passwrd = random.sample(string.ascii_letters, 4)
# passwrd += random.sample(string.digits, 2)
# random.SystemRandom().shuffle(passwrd)
# passwrd = ''.join(passwrd)
# print(passwrd)

# list = []
# cap = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234589'
# for i in range(6):
#     Fcap = random.choice(cap)
#     list.append(Fcap)

# print(list[0], list[1], list[2], list[3], list[4], list[5])


# meg1 = ["Keep your head up, and Don't ever let a bad day define you. We all have them.", "Love can be experienced only by those who are ready to give up their ego.",
#         "No one is too much busy. It’s all about importance you have in their life.", "In your worst days; often you get the help from the one you never expected."]

# print("Meg of The Day:", random.choice(meg1))

