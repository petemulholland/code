from swampy.TurtleWorld import *
import math

# fd & bk for forward & back
# lt & rt for right and left turns
# pu & pd for pen up and down.

def forward_left(turtle, dist, degrees = 90):
    """ Move turtle forward by length and turn left degrees
    """
    fd(turtle, dist)
    lt(turtle, degrees)

def polyline(turtle, length, sides, angle):
    """ move turtle to draw 'sides' number of lines, of length 'length'
        with a left turn of 'degrees' at teh end of each line
    """
    for i in range(sides):
        forward_left(turtle, length, angle)

def polygon(turtle, length, sides):
    """ draw apolygon using turtle of with 'sides' number of side of length 'length'
    """
    angle = 360.0 / sides
    polyline(turtle, length, sides, angle)

def square(turtle, length):
    """ draw a square with sides of length 'length'
    """
    polygon(turtle, length, 4)

def arc(turtle, radius, angle):
    """ draw and arc with radius 'radius' and angle 'angle' in degrees.
    """ 
    # circle values
    moves = radius * 2
    circ = 2 * radius * math.pi
    length = circ / float(moves)
    move_angle = 360.0 / float(moves)
    #reduce to arc
    moves = int(moves * (angle / 360.0))
    polyline(turtle, length, moves, move_angle)

def circle(turtle, radius):
    """ Draw a circle with radius 'radius'
    """
    arc(turtle, radius, 360)


#world = TurtleWorld()
#bob = Turtle()
#bob.delay = 0.01
#print bob

#square(bob, 50)
#square(bob, 100)
#square(bob, 150)
#polygon(bob, 50, 8)
#polygon(bob, 40, 6)
#polygon(bob, 30, 5)
#circle(bob, 50)
#circle(bob, 100)
#circle(bob, 150)
#arc(bob, 50, 90)
#arc(bob, 100, 90)
#arc(bob, 150, 90)

#wait_for_user()
