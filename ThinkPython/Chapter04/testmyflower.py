from mypolygon import *
from myflower import *

def test_petal(turtle):
    petal(turtle, 50, 90)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

#test_petal(bob)
flower(bob, 180, 20, 20)

wait_for_user()
