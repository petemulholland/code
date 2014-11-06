#from swampy.Lumpy import Lumpy

def b(z):
    print "b(", z, ")"
    print "calling a(", z, ",", z,")"
    prod = a(z, z)
    #print z, prod
    print "b returning:", prod
    return prod

def a(x, y):
    print "a(", x, ",", y, ")"
    x = x + 1
    #lumpy.object_diagram()
    result = x * y
    print "a returning:", result
    return result

def c(x, y, z):
    print "c (", x, ",", y, ",", z, ")"
    total = x + y + z
    print "calling b(", total, ")"
    square = b(total)**2
    print "c returning:", square
    return square

#lumpy = Lumpy()
#lumpy.make_reference()

x = 1
y = x + 1
print c(x, y+3, x+y)