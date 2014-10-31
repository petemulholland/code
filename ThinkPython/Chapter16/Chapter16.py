class Time(object):
    """ represents time of day
    attributes: hour, minute, second
    """

def print_time(time):
    print "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)


def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

def create_time(h, m, s):
    t = Time()
    t.hour = h
    t.minute = m
    t.second = s
    return t

def time_tostring(t):
    return "%.2d:%.2d:%.2d" % (t.hour, t.minute, t.second)

def print_is_after(t1, t2):
    print "%s %s %s" % (time_tostring(t1), "is after" if is_after(t1, t2) else "is before", time_tostring(t2))

if __name__ == '__main__':
    time = Time()
    time.hour = 11
    time.minute = 59
    time.second = 30

    print_time(time)

    t1 = create_time(10, 15, 45)
    t2 = create_time(8, 40, 25)
    t3 = create_time(18, 10, 5)

    print_is_after(t1, t2)
    print_is_after(t1, t3)
    print_is_after(t2, t1)
    print_is_after(t2, t3)
    print_is_after(t3, t1)
    print_is_after(t3, t2)
    print_is_after(t1, t1)

