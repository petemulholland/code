def is_palindrome(word, debug=False):
    if debug: print "Checking {0}".format(word),
    return word == word[::-1]

def check_numbers(num, debug=False):    
    # last 4 digits palindromic?
    if not is_palindrome(str(num)[2:], debug):
        if debug: print''
        return False

    num += 1
    # are last 5 nums palindromic?
    if not is_palindrome(str(num)[1:], debug):
        if debug: print''
        return False

    num += 1
    # are middle 4 nums palindromic?
    if not is_palindrome(str(num)[1:5], debug):
        if debug: print''
        return False

    num += 1
    # is entire num palindromic?
    if not is_palindrome(str(num), debug):
        if debug: print''
        return False

    if debug: print''
    return True

def cartalk2(debug = False):
    # 198888
    # 199999
    num = 100000 # no point start with anything less than 6 numbers
    #num = 198884 # no point start with anything less than 6 numbers
    while num < 1000000: # limited to 6 digits
        if check_numbers(num, debug):
            print "{0}, [{1}, {2}, {3}]".format(num, num+1, num+2, num+3)
        
        if debug:
            if num % 10 == 0:
                raw_input("pause")

        if num % 10000 == 0:
            print '.',

        num += 1


if __name__ == '__main__':
    cartalk2(False)
