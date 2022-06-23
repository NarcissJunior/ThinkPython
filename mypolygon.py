import turtle
import math

def square(turtou, length):
    for i in range(500):
        plus = i * 20
        distance = length + plus
        degree = 90

        turtou.fd(distance)
        turtou.lt(degree)


def polygon(turtou, n, length):
    angle = 360.0 / n
    polyline(turtou, n, length, angle)


def circle(turtou, r):
    arc(turtou, r, 360)

def polyline(t, n, length, angle):
    """Desenha n segmentos de reta com o comprimento dado e
    ângulo (em graus) entre eles. t é um turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
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

ninja = turtle.Turtle()

numberPetals = 7
radius = 70
angle = 60
flower(ninja, numberPetals, radius, angle)

#circle(ninja, radius)
#polygon(ninja, length = 50, polygonsize = 5)
#square(ninja, length = 50)
#polyline(ninja, 150, 150, 150)
turtle.mainloop()

##TODO - make an expansive circle :P