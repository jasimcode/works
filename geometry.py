from turtle import *

clr = ["blue", "green", "black", "red"]

pensize(6)

for r in range(100):
    for n in clr:
        color(n)
        rt(1)
        for j in range(1):
            fd(100)
            rt(90)