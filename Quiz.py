from __future__ import print_function

import pyttsx3

print("Welcome to my Quiz")

playing = input("Do you want to play? / Quit ")

if playing.lower() == "quit":
    quit(print("Quiting the game"))

print("Okay! lets play")

score = 0

answer = input("To do Calculations:  ")
if answer.lower() == "calculator":
    print("Correct!")
    score += 1
else:
    print("Incorrect / Wrong spelling")

answer = input("The opposite of empty:   ")
if answer.lower() == "full":
    print("Correct!")
    score += 1
else:
    print("Incorrect / Wrong spelling")

print("Acciddentally, Accidentally, Aciddentally")
answer = input("Bhavika.....spilled ink on the table:    ")
if answer.lower() == "accidentally":
    print("Correct!")
    score += 1
else:
    print("Incorrect / Wrong spelling")

answer = input("To measure our body temprature:  ")
if answer.lower() == "thermometer":
    print("Correct!")
    score += 1
else:
    print("Incorrect / Wrong spelling")

print("Brigde, Birgde, Bridge")
answer = input("The howrah.....is in west bengal:    ")
if answer.lower() == "bridge":
    print("Correct!")
    score += 1
else:
    print("Incorrect / Wrong spelling")

print("You got " + str(score) + " question corect!")
print("You got " + str(score / 5 * 100) + " %.")
