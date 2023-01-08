month = [
    "Months", "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print()
print("Type for coresponding months")
print()
print("January - 1")
print("February - 2")
print("March - 3")
print("April - 4")
print("May - 5")
print("June - 6")
print("July - 7")
print("August - 8")
print("September - 9")
print("October - 10")
print("November - 11")
print("December - 12")
print()

cm = int(input("Type current month:    "))

print()

bm = int(input("Type your birth month:    "))

print()

#maths
birth_day_in = cm - bm
if birth_day_in not in numbers:
    birth_day_in * -1
    print("neg")
elif birth_day_in in numbers:
    birth_day_in * -1
    print("pos")

print()

#print
print(birth_day_in)

print()
