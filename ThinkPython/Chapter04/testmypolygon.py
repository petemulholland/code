from swampy.TurtleWorld import *
from mypolygon import *

def test_square(turtle, count, length):
    for i in range(count):
        square(turtle, length * (i + 1))

def test_polygon(turtle, count, length, sides):
    for i in range(count):
        polygon(turtle, length + (i * 10), sides + i)

def test_circle(turtle, count, radius):
    for i in range(count):
        circle(turtle, radius + (i * 20))

def test_arc(turtle, count, radius, degrees):
    for i in range(count):
        arc(turtle, radius + (i * 20), degrees)

world = TurtleWorld()
bob = Turtle()
print (bob.x, bob.y)
#bob.x -= 50
bob.y -= 50
print (bob.x, bob.y)
bob.delay = 0.01

#test_square(bob, 4, 50)
#test_polygon(bob, 6, 50, 3)
#test_circle(bob, 5, 50)
test_arc(bob, 9, 20, 180)

wait_for_user()
