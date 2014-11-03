class Time(object):
    """ represents time of day
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

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

    def add_time(self, other):
        assert other.is_valid()
        s = self.time_to_int() + other.time_to_int()
        return int_to_time(s)

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

