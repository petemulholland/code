def has_palindrome(i, start, len):
    """Returns True if the integer i, when written as a string,
    contains a palindrome with length (len), starting at index (start).
    """
    s = str(i)[start:start+len]
    return s[::-1] == s
    

def check(i):
    """Checks whether the integer (i) has the properties described
    in the puzzler.
    """
    return (has_palindrome(i, 2, 4)   and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))


def check_all():
    """Enumerates the six-digit numbers and prints any that satisfy the
    requirements of the puzzler"""

    i = 100000
    while i <= 999996:
        if check(i):
            print i
        i = i + 1

if __name__ == '__main__':
    print 'The following are the possible odometer readings:'
    check_all()
    print
