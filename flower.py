import turtle
import math

ninja = turtle.Turtle()

def polyline(t, n, length, angle):
    """Draws n segments of a line based on its length
     and the angle (degree) between them. t is Turtle instance.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Draws and arc using polyline basend on its parameters"""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def petal(turtou, radius, angle):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) of the arcs
    """
    for i in range(2):
        arc(turtou, radius, angle)
        turtou.lt(180 - angle)

def flower(turtou, n, radius, angle):
    """Draws a flower based on a set of petals
    turtou: Turtle
    n: number of petals
    n: radius of the arcs
    angle: angle (degrees) of the arcs
    """
    redirect = 360/n 
    for i in range(n):
        petal(turtou, radius, angle)
        turtou.lt(redirect)

def movePointer(turtou, distance):
    turtou.pu()
    turtou.fd(distance)
    turtou.pd()

numberPetals = 7
radius = 70
angle = 60
movePointer(ninja, -100)
flower(ninja, numberPetals, radius, angle)

numberPetals = 10
radius = 40
angle = 80
movePointer(ninja, 150)
flower(ninja, numberPetals, radius, angle)

numberPetals = 20
radius = 140
angle = 20
movePointer(ninja, 150)
flower(ninja, numberPetals, radius, angle)

ninja.hideturtle()
turtle.mainloop()