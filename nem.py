from turtle import * 
import math
"""
t = turtle.Turtle()

for i in range(4):
    t.left(120)
    t.forward(-120)
    t.forward(120)

turtle.done()
"""
def hearta(a):
    return 15 * math.sin(k)**3

def heartb(b):
    return 12 * math.cos(k) - 3 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)
bgcolor("#0689F4")
color("red", "pink")
penup()

for i in range(6000):
    k = i / 100
    x = hearta(k) * 20
    y = heartb(k) * 20
    goto(x, y)
    pendown()

done()