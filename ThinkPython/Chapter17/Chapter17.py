class Time(object):
    """ represents time of day
    attributes: hour, minute, second
    """

    def print_time(self):
        print "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

    def time_to_int(self): 
        minutes = self.hour * 60 + self.minute 
        seconds = minutes * 60 + self.second 
        return seconds

    def increment(self, seconds):
        assert self.is_valid()
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        assert other.is_valid()
        return self.time_to_int() > other.time_to_int()

    def is_valid(self): 
        if self.hour < 0 or self.minute < 0 or self.second < 0: 
            return False 
        if self.minute >= 60 or self.second >= 60: 
            return False 
        return True

def int_to_time(seconds): 
    time = Time() 
    minutes, time.second = divmod(seconds, 60) 
    time.hour, time.minute = divmod( minutes, 60)
    return time

def ex_17_1():
    time = Time()
    time.hour = 11
    time.minute = 59
    time.second = 30

    time.print_time()

    print 'to int:', time.time_to_int()

if __name__ == '__main__':
    ex_17_1()

    start = Time()
    start.hour = 9
    start.minute = 45
    start.second = 0

    start.print_time()
    end = start.increment(1337)
    end.print_time()

    end.is_after(start)
