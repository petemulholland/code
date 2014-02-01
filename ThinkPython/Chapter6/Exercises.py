import math

def compare(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0


#print 'compare 3 and 4: ', compare(3, 4)
#print 'compare 5 and 4: ', compare(5, 4)
#print 'compare 4 and 4: ', compare(4, 4)

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsqd = dx ** 2 + dy ** 2
    result = math.sqrt(dsqd)
    return result

#distance(1, 2, 4, 6)

def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def area(radius): 
    return math.pi * radius** 2 


#hypotenuse(3, 4)

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

#circle_area(1, 2, 4, 6)

def is_between(x, y, z):
    return x <= y and y <= z

def factorial(x):
    if x <= 0:
        return 1
    else:
        return x * factorial(x - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



