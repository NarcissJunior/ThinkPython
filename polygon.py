import turtle
import math

def square(t, length):
    """Draws a square with sides of the given length.
    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(turtou, n, length):
    """Draws a polygon based on length and with n sides"""
    angle = 360.0 / n
    polyline(turtou, n, length, angle)

def polyline(t, n, length, angle):
    """Draws n line segments.
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def movePointer(turtou, distance):
    turtou.pu()
    turtou.fd(distance)
    turtou.pd()

def circle(t, r):
    """Draws a circle with the given radius.
    r: radius
    """
    arc(t, r, 360)


if __name__ == '__main__':

    turtou = turtle.Turtle()

    radius = 100
    turtou.pu()
    turtou.fd(radius)
    turtou.lt(90)
    turtou.pd()
    circle(turtou, radius)

    turtou.hideturtle()
    turtle.mainloop()