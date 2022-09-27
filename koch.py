import turtle

donatello = turtle.Turtle()

def koch_curve(don, len):
        don.fd(len)
        don.lt(60)
        don.fd(len)
        don.rt(120)
        don.fd(len)
        don.lt(60)
        don.fd(len)


def koch_line(don, len):
    koch_curve(don, len)
    don.lt(60)
    koch_curve(don, len)
    don.rt(120)
    koch_curve(don, len)
    don.lt(60)
    koch_curve(don, len)
    don.lt(60)
    koch_curve(don, len)
    don.lt(60)
    koch_curve(don, len)
    don.rt(120)
    koch_curve(don, len)
    don.lt(60)
    koch_curve(don, len)
    don.rt(120)
    koch_curve(don, len)
    don.lt(60)
    koch_curve(don, len)
    don.rt(120)
    koch_curve(don, len)
    don.lt(60)
    koch_curve(don, len)
    don.lt(60)
    koch_curve(don, len)
    don.lt(60)
    koch_curve(don, len)
    don.rt(120)
    koch_curve(don, len)
    don.lt(60)
    koch_curve(don, len)

def koch_triangle(don, length, n):
    #todo
    if n < 3:
        if (2 % n) == 0:
            koch_line(don, length)
            don.lt(60)
        else:
            koch_line(don, length)
            don.rt(120)
        koch_triangle(don,length, n+1)
    else:
        return

    # koch_line(don, length)
    # don.lt(60)
    # koch_line(don, length)
    # don.rt(120)
    # koch_line(don, length)
    # don.lt(60)
    # koch_line(don, length)

def draw_koch(don, length, n):
    if n < 2:
        koch_triangle(don, length, 1)
        don.rt(120)
        draw_koch(don, length, n+1)
    else:
        return

length = 5
n = 0
draw_koch(donatello, length, n)

donatello.hideturtle()
turtle.mainloop()