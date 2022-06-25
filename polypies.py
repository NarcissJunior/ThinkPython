import turtle
import math

def draw_pie(t, n, r):
    """Draws a pie, then moves into position to the right.
    n: number of segments
    r: length of the radial spokes
    """
    polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()

def polypie(t, n, r):
    """Draws a pie divided into radial segments.
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        triangle(t, r, angle/2)
        t.lt(angle)

def triangle(t, r, angle):
    """Draws an icosceles triangle.
    r: length of the equal legs
    angle: half peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

turtou = turtle.Turtle()

#Draw the polygons
size = 40
draw_pie(turtou, 5, size)
draw_pie(turtou, 6, size)
draw_pie(turtou, 7, size)
draw_pie(turtou, 8, size)

turtou.hideturtle()
turtle.mainloop()