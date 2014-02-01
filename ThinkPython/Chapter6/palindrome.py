def first(word): 
    return word[0] 

def last(word): 
    return word[-1] 

def middle(word): 
    return word[1:-1]

#print "middle('ab') returns [", middle('ab'), "]"
#print "middle('a') returns [", middle('a'), "]"
#print "middle('') returns [", middle(''), "]"

def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        if first(s) != last(s):
            return False
        else:
            return is_palindrome(middle(s))

is_palindrome('a')
is_palindrome('ab')