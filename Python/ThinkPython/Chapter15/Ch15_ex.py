from Chapter15 import Rectangle
from Chapter15 import Point
from swampy.World import World

def draw_rect(canvas, rect):
    bbox = [[rect.corner.x, rect.corner.y], [rect.corner.x + rect.width, rect.corner.y + rect.height]]
    canvas.rectangle(bbox, outline='black', width=2, fill=rect.color)

def draw_point(canvas, point):
    canvas.circle([point.x,point.y], 5, outline=None, fill='black')

def draw_circle(canvas, circle):
    canvas.circle([circle.center.x,circle.center.y], circle.radius, outline=None, fill='red')


def create_point(x, y):
    pt = Point()
    pt.x = x
    pt.y = y
    return pt

def create_rect(x, y, w, h):
    rect = Rectangle()
    rect.width = w
    rect.height = h
    rect.corner = create_point(x, y)
    return rect

class Circle(object):
    """Represents a circle."""

def create_circle(x, y, r):
    c = Circle()
    c.radius = r
    c.center = create_point(x, y)
    return c


def ex_15_4_1(canvas):
    box = Rectangle()
    box.width = 300
    box.height = 200
    box.corner = Point()
    box.corner.x = -150
    box.corner.y = -100

    box.color = 'green4'

    draw_rect(canvas, box)
    
    pt = Point()
    pt.x = -25
    pt.y = 0

    draw_point(canvas, pt)

def ex_15_4_4(canvas):
    c1 = create_circle(25, 50, 10)
    draw_circle(canvas, c1)
    c2 = create_circle(-50, 30, 40)
    draw_circle(canvas, c2)
    c3 = create_circle(30, -60, 60)
    draw_circle(canvas, c3)

def ex_15_4_5(canvas):
    rw = create_rect(-150, 0, 300, 100)
    rw.color = 'white'
    rr = create_rect(-150, -100, 300, 100)
    rr.color = 'red'

    draw_rect(canvas, rw)
    draw_rect(canvas, rr)

    points = [[-150,-100], [-150, 100], [0, 0]] 
    canvas.polygon(points, fill='blue')


if __name__ == '__main__':
    world = World()
    canvas = world.ca(width=500, height=500, background='white')

    #ex_15_4_4()
    ex_15_4_5(canvas)

    world.mainloop()