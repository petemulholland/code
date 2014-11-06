import math
import copy

class Point(object):
    """Represents a point in 2D space."""


def print_point(p):
    print '(%g, %g)' % (p.x, p.y)

def point_tostring(p):
    return '(%g, %g)' % (p.x, p.y)

def distance_between_points(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def ex_15_1():
    blank = Point()
    blank.x = 3.0
    blank.y = 4.0

    p1 = Point()
    p1.x = 1.0
    p1.y = 1.0

    p0 = Point()
    p0.x = 0.0
    p0.y = 0.0

    print 'Distance between ', point_tostring(p0), ' and ', point_tostring(blank), ' is ', distance_between_points(p0, blank)
    print 'Distance between ', point_tostring(p1), ' and ', point_tostring(blank), ' is ', distance_between_points(p1, blank)

class Rectangle(object):
    """represents a rectangle
    attributes: width, height, corner
    corner => lower right
    """

def print_rect(rect):
    print 'center', point_tostring(find_center(rect)), 'width', rect.width, 'height', rect.height


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def move_rectangle2(rect, dx, dy):
    newrect = copy.deepcopy(rect)
    move_rectangle(newrect, dx, dy)
    return newrect

def ex_15_2():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print_rect(box)

    grow_rectangle(box, 50, 100)

    print_rect(box)

    move_rectangle(box, 50, 100)

    print_rect(box)

def ex_15_3():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print_rect(box)
    newbox = move_rectangle2(box, 50, 100)

    print_rect(box)
    print_rect(newbox)

if __name__ == '__main__':
    #ex_15_1()
    #ex_15_2()
    ex_15_3()
