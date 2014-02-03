from swampy.TurtleWorld import *
import math

# BEGIN Exercise 5-2
def do_n(f, n):
    if n <= 0:
        return
    f()
    do_n(f, n -1)


def fn():
    print "fn()"


def test_fn(n):
    do_n(fn, n)


#test_fn(3)
# END Exercise 5-2

# BEGIN Exercise 5-3
def check_fermat(a, b, c, n):
    an = math.pow(a, n)
    bn = math.pow(b, n)
    cn = math.pow(c, n)

    if (an + bn) == cn:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work"

def run_fermat_check():
    a = int(raw_input("Enter a: "))
    b = int(raw_input("Enter b: "))
    c = int(raw_input("Enter c: "))
    n = int(raw_input("Enter n: "))
    
    check_fermat(a, b, c, n)

#run_fermat_check()

# END Exercise 5-3

# BEGIN Exercise 5-4
def is_triangle(a, b, c):
    if (c > a + b) or (b > a + c) or (a > b + c):
        print "No"
    else:
        print "Yes"

def run_triangle_check():
    a = int(raw_input("Enter length #1: "))
    b = int(raw_input("Enter length #2: "))
    c = int(raw_input("Enter length #3: "))
    
    is_triangle(a, b, c)

#run_triangle_check()

# END Exercise 5-4

# BEGIN Exercise 5-4
def draw( t, length, n): 
    if n == 0: 
        return 
    angle = 50 
    fd( t, length* n) 
    lt( t, angle) 
    
    draw( t, length, n-1) 
    
    rt( t, 2* angle) 
    
    draw( t, length, n-1) 
    
    lt( t, angle) 
    bk( t, length* n)

# END Exercise 5-4

# BEGIN Exercise 5-5
def koch(t, x, div):
    if x < div:
        fd(t, x)
        return

    koch(t, x / div, div)
    lt(t, 60)
    koch(t, x / div, div)
    rt(t, 120)
    koch(t, x / div, div)
    lt(t, 60)
    koch(t, x / div, div)

def do_koch(t, div, exp):
    koch(t, math.pow(div, exp) - 1, div)

def do_snowflake(t, div, exp):
    do_koch(t, div, exp)
    rt(t, 120)
    do_koch(t, div, exp)
    rt(t, 120)
    do_koch(t, div, exp)
    
# BEGIN Exercise 5-5

world = TurtleWorld(False, 1000, 400)
bob = Turtle()
print (bob.x, bob.y)
bob.x -= 150
bob.y += 50
bob.delay = 0

div = 3
exp = 5
do_snowflake(bob, div, exp)