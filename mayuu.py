from __future__ import print_function

score = 0

print()
print("Welcome to my Quiz")
print()

playing = input("Do you want to play? (Ok/Quit) :   ")

if playing.lower() == "quit":
    quit(print("Quiting the game"))

print()
print("Okay! lets play")
print()

print("Q1 : AB and AC are tangents AB=5cm")
print("What is the length of AC")
answer = input("Type your answer :  ").lower()
if answer == "5cm":
    print()
    print("correct")
    print()
    score=+1
else:
    print("wrong!!")
print("Q2 : The ore of which metal is clamine")
print("(Aluminium, Zinc, Copper, Iron)")
answer = input("Type your answer :  ").lower()
if answer == "zinc":
    print()
    print("correct")
    print()
    score=+1
else:
    print("wrong!!")
print("Q3 : Who was the chairman of linguistic reorganization commission")
answer = input("Type your answer :  ").lower()
if answer == "fazl ali":
    print()
    print("correct")
    print()
    score=+1
else:
    print("wrong!!")
print("Q4 : From which tax comes under central government")
print("(Land tax, Property tax, Corporate tax, Stamp duty)")
answer = input("Type your answer :  ").lower()
if answer == "corporate tax":
    print()
    print("correct")
    print()
    score=+1
else:
    print("wrong!!")
print("Q5 : Who is the auther of the stroy 'Adventures in a Banyan Tree'")
answer = input("Type your answer :  ").lower()
if answer == "ruskin bond":
    print()
    print("correct")
    print()
    score=+1
else:
    print("wrong!!")
print("Q6 : The midpoint of a lens is known as ___")
print("(Optic centre, Principle focus, center of curvature)")
answer = input("Type your answer :  ").lower()
if answer == "optic centre":
    print()
    print("correct")
    print()
    score=+1
else:
    print("wrong!!")
print("Q7 : What is bacterial disease for paddy")
answer = input("Type your answer :  ").lower()
if answer == "blight":
    print()
    print("correct")
    print()
    score=+1
else:
    print("wrong!!")
print("Q8 : What is fullform of HTML")
answer = input("Type your answer :  ").lower()
if answer == "hyper text markup language":
    print()
    print("correct")
    print()
    score=+1
else:
    print("wrong!!")

print("You got " + str(score) + " question corect!")
print("You got " + str(score / 8 * 100) + " %.")