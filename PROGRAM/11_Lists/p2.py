import turtle
import math
import random

s = turtle.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)

colors = ["red", "magenta", "pink", "cyan", "yellow", "blue"]

for i in range(140):
    a = i * 2 * math.pi / 140

    x = 16 * math.sin(a) ** 3
    y = 13 * math.cos(a) - 5 * math.cos(2*a) - 2 * math.cos(3*a) - math.cos(4*a)

    x *= 15
    y *= 15

    t.penup()
    t.goto(0, 30)
    t.setheading(t.towards(x, y))
    t.color(colors[i % len(colors)])
    t.pendown()

    d = math.sqrt(x*x + (y-30)*(y-30))

    for j in range(int(d / 14)):
        t.forward(8)
        t.penup()
        t.forward(5)
        t.pendown()

    if i % 4 == 0:
        s.update()

s.update()
turtle.done()