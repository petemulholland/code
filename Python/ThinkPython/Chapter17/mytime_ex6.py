class Time(object):
    """ represents time of day
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        minutes = hour * 60 + minute 
        self.seconds = minutes * 60 + second 

    def __str__(self):
        minutes, second = divmod(self.seconds, 60) 
        hour, minute = divmod(minutes, 60)
        return "%.2d:%.2d:%.2d" % (hour, minute, second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def print_time(self):
        print str(self)

    def time_to_int(self):
        return self.seconds

    def increment(self, seconds):
        assert self.is_valid()
        s = self.seconds + seconds
        return int_to_time(s)

    def add_time(self, other):
        assert other.is_valid()
        s = self.time_to_int() + other.time_to_int()
        return int_to_time(s)

    def is_after(self, other):
        assert other.is_valid()
        return self.time_to_int() > other.time_to_int()

    def is_valid(self): 
        return self.seconds >= 0 and self.seconds < 60*60*24

    # Ex 18.1 integer subtraction
    def __cmp__(self, other):
        return self.seconds - other.seconds

def int_to_time(seconds): 
    time = Time(0, 0, seconds) 
    return time


## should ouput following:
# 09:45:00
# 10:07:17
# Is end after start? True
# Using __str__
# 09:45:00 10:07:17
# 11:20:00
# 10:07:17
# 10:07:17
# Example of polymorphism
# 23:01:00

def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print 'Is end after start?',
    print end.is_after(start)

    print 'Using __str__'
    print start, end

    start = Time(9, 45)
    duration = Time(1, 35)
    print start + duration
    print start + 1337
    print 1337 + start

    print 'Example of polymorphism'
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print total

def cmp_to_string(res):
    if res > 0:
        return ">"
    if res < 0:
        return "<"
    return "="

def ex_18_1():
    t1 = Time(9, 45, 00)
    t2 = Time(9, 45, 00)
    t3 = Time(11, 25, 30)

    print t1, cmp_to_string(cmp(t1, t2)), t2
    print t1, cmp_to_string(cmp(t1, t3)), t3
    print t3, cmp_to_string(cmp(t3, t2)), t2


if __name__ == '__main__':
    #main()
    ex_18_1()
