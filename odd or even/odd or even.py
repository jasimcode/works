import random

number = [1, 2, 3, 4, 5, 6]
odd_pick = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
even_pick = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 27, 28, 30]

computer_pick = random.randint(1, 6)

print("default your are batting")

while True:
    user_score = 0
    computer_score = 0

    user_pick = int(input("Type number from 1 to 6 :   "))

    user_score + user_pick

    print(user_score)

    if user_pick == 2:
        quit()

print("user = " + user_score, "computer = " + computer_pick)
runs = user_score + user_pick
print(runs)