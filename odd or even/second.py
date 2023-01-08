import random

user_score = 0
computer_score = 0

number = [1, 2, 3, 4, 5, 6]
odd_pick = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
even_pick = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 27, 28, 30]
types = ["odd", "even"]
modes = ["Bating", "Balling"]
computer_pick = random.randint(1, 6)
computer_mode = random.randint(0, 1)

user_input = str(input("Type odd or even -  "))

if user_input == types[0]:
    user_pick = int(input("Type a number from 1 to 6 -  "))
    odd = user_pick + computer_pick
elif user_input == types[1]:
    user_pick = int(input("Type a number from 1 to 6 -  "))
    even = user_pick + computer_pick

if odd in odd_pick:
    print("your turn odd")
elif odd in even_pick:
    print("PC's turn")
if even in even_pick:
    print("your turn even")
elif even in odd_pick:
    print("PC's turn")