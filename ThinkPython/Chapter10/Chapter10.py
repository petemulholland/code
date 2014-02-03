import random
import datetime

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
    pass

def list_words2(fin):
    pass

def test_list_words():
    fin = open('..\words.txt') 

    start = datetime.timetz()
    list_words1(fin)
    end = datetime.timetz()

    print "list_words1 took:", end - start
    fin.close

    fin = open('..\words.txt') 

    start = datetime.timetz()
    list_words2(fin)
    end = datetime.timetz()

    print "list_words2 took:", end - start

    fin.close



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
    test_list_words()