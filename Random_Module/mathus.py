import random
import string
import math


def redian():
    pi = 22/7

    degree = float(input("Input Degree:-"))

    redian = (pi/180)*degree
    print(redian)

# print(---------------------------------------------------------------------------------------------->)


def lotterynum():
    print("Genrate 3 random numbers beetween 100 to 999 is Divaided by 5 :-")

    for num in range(3):
        print(random.randrange(100, 999, 5))

    lotrry_list = []

    for i in range(100):
        lotrry_list.append(random.randrange(1000000000, 9999999999))

    winner = random.sample(lotrry_list, 2)
    print("The Winner of the Prize are:-", winner)

# print(---------------------------------------------------------------------------------------------->)


def otpgenratr():
    otp = []
    for i in range(6):
        otp.append(random.randrange(100000, 999999))
    print(otp)

# print(---------------------------------------------------------------------------------------------->)


H = "HariomPatidar"

print("The Random number is:-", random.choice(H))

# print(---------------------------------------------------------------------------------------------->)


def RansdomString(Length_String):
    latters = string.ascii_letters
    return ''.join(random.choice(latters) for i in range(Length_String))

    Length_String = input("Enter length")
    print("The random string is:-")

# print(---------------------------------------------------------------------------------------------->)


def RandomPassword():
    PasswordSourse = string.ascii_letters+string.digits+string.punctuation
    password = random.sample(PasswordSourse, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    Passwordlist = list(password)
    random.SystemRandom().shuffle(Passwordlist)
    password = ''.join(Passwordlist)
    return password

# print(---------------------------------------------------------------------------------------------->)


def randomnum():
    num1 = random.random()
    num2 = random.uniform(9.5, 99.5)
    r = num1*num2
    print(r)
    # print(computer)

# print(---------------------------------------------------------------------------------------------->)


def choicegame():
    player = float(input("Enter Your Number beetween 1 to 6:-"))
    if player in range(0, 7):
        computer = [1, 2, 3, 4, 5, 6]

        c = random.choice(computer)
        print("computer genret", c)
        if player == c:
            print("The match is Tie")
        elif player > c:

            print("You Won")
        else:
            print("You Loose")

# print(---------------------------------------------------------------------------------------------->)


def rockpaprsisor():
    player_action = int(
        input("Please Enter Your :\n1= Rock,2=Paper,3=Scissor:"))
    Posible_actions = ["Rock", "Paper", "Scissor"]
    computer_action = random.choice(Posible_actions)

    print(f"\nYou Chose {player_action},And Computer chose {computer_action}")

    if player_action == computer_action:
        print("It's Tie")
    elif player_action == 1:
        if computer_action == 'Paper':
            print("Paper Covers Rock ,You Lose.")
        else:
            print("Rock Smashes Scissor!You Win!")
    elif player_action == 2:
        if computer_action == 'Rock':
            print("Paper Cover the Rock! You Win!")
        else:
            print("Scissors Cut The Paper!You Lose.")
    elif player_action == 3:
        if computer_action == 'Paper':
            print("Scissor Cut The Paper! You Lose. ")
        else:
            print("Rock Smashes Scissor! You Lose.")

# print(---------------------------------------------------------------------------------------------->)


def lotrryTicket():
    for i in range(3):
        a = random.randrange(100, 999, 5)
        print(a)

    lottry_Tickits = []
    for i in range(10):
        lottry_Tickits.append(random.randrange(100000000, 9999999999))
        print(lottry_Tickits)


Winner = random.sample(lottry_Tickits, 2)
print("Winner is:", Winner)

# print(---------------------------------------------------------------------------------------------->)

for i in range(3):
    a = random.randrange(100000, 999999)
print(a)

S1 = "HariomPatidar"
a = random.choice(S1)
print(a)

# print(---------------------------------------------------------------------------------------------->)


def randomPassword():
    randomsourse = string.ascii_letters + string.digits+string.punctuation
    password = random.sample(randomsourse, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    passwordli = list(password)
    random.SystemRandom().shuffle(passwordli)
    password = ''.join(passwordli)
    return password


print("Password is:")

a = "HariomPatidar"
print(len(a))

# print(---------------------------------------------------------------------------------------------->)
