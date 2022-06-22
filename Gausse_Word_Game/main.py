from random import *

name = input("Enter Your Name=\n")
print("Hey {} ".format(name))

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(word)
print("Gessus a Character=\n")
gessuses = ''
turns = 10
while turns > 0:
    failed = 0
    if char in word:
        if char in gessuses:
            print(char, end=" ")
        else:
            print("_")
            print(char, end=" ")
            failed += 1
    if failed == 0:
        print("You Win!!!")
        print("The Word is-", word)
    print()
    gusses = input("Guess a Character=\n")
    gessuses += gusses
    if gusses in word:
        turns -= 1
        print("Wrong")
        print("You Have", +turns, "More Gusses")
        if turns == 0:
            print("You Loose")
