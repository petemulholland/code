import random
import time

# exercise 10-1
def nested_sum(ints):
    """ takes a nested list of integers and add up the elements from all of the nested lists.
        assuming on 1 level of nesting
    """
    total = 0
    for i in range(len(ints)):
        total += sum(ints[i])

    return total

def test_nested_sum():
    test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print nested_sum(test)


# exercise 10-2
def capitalize_nested(t): 
    """ takes a nested list of strings and returns a new nested list with all strings capitalized.
        assuming on 1 level of nesting
    """
    res = [] 
    for n in t: 
        nested = []
        for o in n:
            nested.append(o.capitalize())

        res.append(nested) 
    
    return res


def test_capitalize_nested():
    test = [['do', 're', 'me'], ['fah', 'soh', 'la'], ['tee', 'doh']]
    print capitalize_nested(test)


# exercise 10-3
def cumulative_sum(t):
    """takes a list of numbers and returns the cumulative sum;"""
    res = []
    total = 0
    for num in t:
        total += num
        res.append(total)

    return res

def test_cumulative_sum():
    test = [1, 2, 3]
    print cumulative_sum(test)


# exercise 10-4
def middle(t):
    """takes a list and returns a new list that contains all but the first and last elements."""
    return t[1:-1]

def test_middle():
    test = [1, 2, 3, 4]
    print middle(test)
    test = [1, 2, 3]
    print middle(test)
    test = [1, 2]
    print middle(test)

# exercise 10-5
def chop(t):
    if len(t) > 0:
        del t[0]

    if len(t) > 0:
        del t[-1]

def test_chop():
    test = [1, 2, 3, 4]
    print chop(test), test
    test = [1, 2, 3]
    print chop(test), test
    test = [1, 2]
    print chop(test), test

    test = [1]
    print chop(test), test


# exercise 10-6
def is_sorted(t):
    """is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise."""
    return t == sorted(t)

def test_is_sorted():
    t = [1, 2, 3]
    print t, is_sorted(t), t
    t = [4, 1, 2, 3]
    print t, is_sorted(t), t

# exercise 10-7
def is_anagram(t1, t2):
    """that takes two strings and returns True if they are anagrams."""
    return sorted(t1) == sorted(t2)

def test_is_anagram():
    t1 = 'peter'
    t2 = 'treep'
    print t1, "is an anagram of", t2, ":", is_anagram(t1, t2)
    t3 = 'traap'
    print t1, "is an anagram of", t3, ":", is_anagram(t1, t3)

# exercise 10-8
def has_duplicates(t):
    s = sorted(t)
    for i in range(len(s) -1):
        if s[i] == s[i + 1]:
            return True

    return False

def random_bday():
    year = 2014
    month = random.randint(1, 12)
    day = 1
    if month == 2:
        day = random.randint(1, 28)
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)

    return datetime.date(year, month, day)

def random_bdays(count):
    res = []
    for i in range(count):
        res.append(random_bday())

    return res

def test_has_duplicates():
    simulations = 1000
    students = 23
    count = 0
    
    for i in range(simulations):
        dates = random_bdays(students)
        if has_duplicates(dates):
            count += 1

    print "With %d simulations" % simulations, "of %d students" % students, "there were %d duplicates" % count

# exercise 10-9
def remove_duplicates(t):
    s = sorted(t)
    dupes = []
    # find dupes
    for i in range(len(s) -1):
        if s[i] == s[i + 1]:
            dupes.append(i)

    # remove dupes from end first, back to start
    dupes.reverse()
    for i in dupes:
        del s[i]

    return s

def test_remove_duplicates():
    test = [2, 4, 6, 5, 4, 3, 7, 4, 2, 3, 8, 4, 6]
    print remove_duplicates(test)


# exercise 10-10
def list_words1(fin):
    words = []
    for line in fin: 
        word = line.strip()
        words.append(word)


def list_words2(fin):
    words = []
    for line in fin: 
        word = line.strip()
        words = words + [word]


def test_list_words():
    fin = open('..\words.txt') 

    start = time.time()
    list_words1(fin)
    elapsed = time.time() - start

    print "list_words1 took:", elapsed
    fin.close

    fin = open('..\words.txt') 

    start = time.time()
    list_words2(fin)
    elapsed = time.time() - start

    print "list_words2 took:", elapsed

    fin.close

# exercise 10-11
def read_words():
    fin = open('..\words.txt') 
    words = []
    for line in fin: 
        word = line.strip()
        words.append(word)

    return words

#TODO: read documentaiton on bisect module and look at bisect_left used in book soln.
def bisect(words, target):
    start = 0
    end = len(words) - 1
    while start < end:
        mid = ((end - start) / 2) + start
        if words[mid] == target:
            return mid

        if words[mid] < target:
            if start == mid: return
            start = mid
        else:
            if end == mid: return
            end = mid

    return None

def test_bisect():
    target = 'loppier'
    words = read_words()
    idx = bisect(words, target)
    if idx == None:
        print "Word", target, "was not found"
    else:
        print "Word", target, "was found at index", idx

# exercise 10-12
def reverse_pairs():
    words = read_words()
    for word in words:
        rev = word[::-1]
        if bisect(words, rev) != None:
            print word, rev
        
    


# exercise 10-13
def find_interlocked_pairs():
    words = read_words()
    for word in words:
        wd1 = word[0::2]
        wd2 = word[1::2]
        if bisect(words, wd1) != None and bisect(words, wd2) != None:
            print "'{0}' and '{1}' interlock to give '{2}'".format(wd1, wd2, word)
            #print "'",wd1, "and", wd2, "interlock to give", word

def find_interlocked_triples():
    words = read_words()
    for word in words:
        wd1 = word[0::3]
        wd2 = word[1::3]
        wd3 = word[2::3]
        if bisect(words, wd1) != None and bisect(words, wd2) != None and bisect(words, wd3) != None:
            print "'{0}', '{1}' and '{2}' interlock to give '{3}'".format(wd1, wd2, wd3, word)
            #print "'",wd1, "and", wd2, "interlock to give", word

if __name__ == '__main__':
    #test_nested_sum()
    #test_capitalize_nested()
    #test_cumulative_sum()
    #test_middle()
    #test_chop()
    #test_is_sorted()
    #test_is_anagram()
    #test_has_duplicates()
    #test_remove_duplicates()
    #test_list_words()
    #test_bisect()
    #reverse_pairs()
    #find_interlocked_pairs()
    find_interlocked_triples()