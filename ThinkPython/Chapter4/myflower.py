from mypolygon import *

def petal(turtle, radius, angle):
    for i in range(2):
        arc(turtle, radius, angle)
        lt(turtle, 180 - angle)

def flower(turtle, radius, angle, petals):
    turn = 360.0 / petals
    for i in range(petals):
        petal(turtle, radius, angle)
        lt(turtle, turn)
