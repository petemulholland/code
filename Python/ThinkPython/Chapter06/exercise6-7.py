def is_power(a, b):
    if a < b:
        return False
    elif a == b:
        return True
    elif a % b == 0:
        return is_power(a/b, b)
    else:
        return False



def gcd(a, b):
    print "gcd(", a, ",", b, ")"
    if b == 0:
        return a

    r = a % b
    return gcd(b, r)
