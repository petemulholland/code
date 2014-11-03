from mytime import *
from mypoint import *

import Debug

def ex_17_1():
    start = Time(9, 45)
    start.print_time()
    print 'to int:', start.time_to_int()

    end = start.increment(1337)
    end.print_time()

    end.is_after(start)

    time = Time()
    time.print_time()

    print start
    print end
    print time

def ex_17_2():
    p1 = Point()
    print p1
    p2 = Point(3, 4)
    print p2

    print p1, p2

def ex_17_4():
    start = Time(9, 45)
    duration = Time(1, 35)
    print start, '+', duration, '=', start + duration
    print start, '+ 1337 =', start + 1337

    print '1337 +', start, '=', 1337 + start

    print start.__dict__
    Debug.print_attributes(start)

    pt1 = Point(2, 3)
    pt2 = Point(1, 1)
    print pt1, '+', pt2, '=', pt1 + pt2

    print pt1, pt2 # verify neither has changed.

    coords = (2, 2)

    print pt1, '+', coords, '=', pt1 + coords
    print pt1.__dict__
    Debug.print_attributes(pt1)


if __name__ == '__main__':
    #ex_17_1()
    #ex_17_2()
    ex_17_4()

