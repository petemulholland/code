from datetime import *

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

def ex_16_2():
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

def increment_from_book(time, seconds): 
    time.second += seconds 
    
    if time.second >= 60: 
        time.second -= 60 
        time.minute += 1

    if time.minute >= 60: 
        time.minute -= 60 
        time.hour += 1

def increment(time, seconds):
    time.second += seconds

    time.minute += time.second / 60
    time.second = time.second % 60

    time.hour += time.minute / 60
    time.minute = time.minute % 60

def ex_16_3():
    t = create_time(8, 40, 25)
    increment_from_book(t, 1340)
    print_time(t)

    t = create_time(8, 40, 25)
    increment(t, 1340)
    print_time(t)

def pure_increment(time, seconds):
    t = create_time(time.hour, time.minute, time.second)
    t.second += seconds

    minutes, t.second = divmod(t.second, 60) 
    t.minute += minutes

    hours, t.minute = divmod(t.minute, 60)
    t.hour += hours
    return t

def ex_16_4():
    t = create_time(8, 40, 25)
    t2 = pure_increment(t, 1340)
    print_time(t)
    print_time(t2)


def time_to_int(time): 
    minutes = time.hour * 60 + time.minute 
    seconds = minutes * 60 + time.second 
    return seconds

def int_to_time(seconds): 
    time = Time() 
    minutes, time.second = divmod(seconds, 60) 
    time.hour, time.minute = divmod( minutes, 60)
    return time

def add_time(t1, t2): 
    assert valid_time(t1) and valid_time(t2) 
    seconds = time_to_int(t1) + time_to_int(t2) 
    return int_to_time(seconds)

def increment_v3(time, seconds):
    assert valid_time(time)
    s = time_to_int(time) + seconds
    return int_to_time(s)

def ex_16_5():
    t = create_time(8, 40, 25)
    t2 = increment_v3(t, 1340)
    print_time(t)
    print_time(t2)


def valid_time(time): 
    if time.hour < 0 or time.minute < 0 or time.second < 0: 
        return False 
    if time.minute >= 60 or time.second >= 60: 
        return False 
    return True

def mul_time(t, mul):
    s = time_to_int(t) * mul
    return int_to_time(s)

def avg_time(duration, distance):
    return mul_time(duration, (1.0 / distance))

def ex_16_6():
    t1 = create_time(1, 15, 24)
    t2 = mul_time(t1, 2)
    print_time(t1)
    print_time(t2)

    t3 = create_time(2, 46, 24)
    t4 = avg_time(t3, 26)
    print_time(t3)
    print_time(t4)


def print_day_of_week():
    dt = date.today()
    print 'Day of week', dt.weekday()

def birthday(bday):
    tday = date.today()

    age = tday - bday
    print 'You are ', age.days / 365, ' years old'

    next_bday = date(tday.year, bday.month, bday.day)
    if next_bday < tday:
        next_bday = date(tday.year + 1, bday.month, bday.day)

    next_bday = datetime.combine(next_bday, time.min)

    to_next_bday = next_bday - datetime.today()

    print 'Next birthday in: ', to_next_bday

def double_day(date1, date2):
    diff = 0
    if date1 > date2:
        diff = date1 - date2
        print 'Double day:', date1 + diff
    else:
        diff = date2 - date1
        print 'Double day:', date2 + diff

def ex_16_7():
    print_day_of_week()

    bday = date(1972, 10, 11)
    birthday(bday)

    me = date(1972, 10, 11)
    mick = date(1974, 02, 27)

    double_day(me, mick)
    double_day(mick, me)


if __name__ == '__main__':
    #ex_16_2()
    #ex_16_3()
    #ex_16_4()
    #ex_16_5()
    #ex_16_6()
    ex_16_7()
