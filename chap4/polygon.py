from __future__ import print_function, division

import math
import turtle

pi = 3.14

def square(aTurtle: turtle.Turtle, length: int):
    for i in range(4):
        aTurtle.lt(90)
        aTurtle.fd(length)


def polygon(aTurtle: turtle.Turtle, length: int, n: int):
    for i in range(n):
        aTurtle.lt(360/n)
        aTurtle.fd(length)


def arc(aTurtle: turtle.Turtle, radius: int, angle: int):
    circ = 2 * pi * radius
    for i in range(angle):
        aTurtle.lt(1)
        aTurtle.fd(circ/360.0)


def circle(aTurtle: turtle.Turtle, radius: int):
    circ = 2 * pi * radius
    for i in range(360):
        aTurtle.lt(1)
        aTurtle.fd(circ/360.0)


if __name__ == '__main__':
    bob = turtle.Turtle()
    # square(bob, 200)
    # polygon(bob, 200, 5)
    # circle(bob, 100)
    arc(bob, 100, 90)

    # draw a circle centered on the origin
    # radius = 100
    # bob.pu()
    # bob.fd(radius)
    # bob.lt(90)
    # bob.pd()
    # circle(bob, radius)

    # wait for the user to close the window
    turtle.mainloop()
