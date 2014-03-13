import random

def sumall(*args):
    sum = 0
    for num in args:
        sum += num

    return sum

def ex_12_01():
    print "sumall(1, 2, 3)", sumall(1, 2, 3)
    print "sumall(1, 2, 3, 4)", sumall(1, 2, 3, 4)
    print "sumall(1, 2, 3, 4, 5)", sumall(1, 2, 3, 4, 5)
    print "sumall(1, 2, 3, 4, 5, 6)", sumall(1, 2, 3, 4, 5, 6)


def sort_by_length_random(words): 
    t = [] 
    word_ct = len(words)
    for word in words: 
        t.append((len(word), random.randint(0,word_ct), word)) 
        
    t.sort( reverse = True) 
    
    res = [] 
    for length, rnd, word in t: 
        res.append( word) 
        
    return res


def ex_12_02():
    words = ['John', 'Eric', 'Graham', 'Gerry', 'Terry', 'Peter', 'Michael', 'Mick']

    t = sort_by_length_random(words)
    for x in t:
        print x

    print

def most_frequent(t):
    l = tuple(t)
    d = dict()
    for letter in l:
        if letter.isalpha():
            if not d.has_key(letter):
                d[letter] = 1
            else:
                d[letter] += 1

    t2 = zip(d.values(), d.keys())
    t2.sort(reverse=True)

    return t2


def ex_12_03():
    print most_frequent("The quick brown fox jumps over the lazy dog")


def read_words():
    fin = open('..\words.txt') 
    words = []
    for line in fin: 
        word = line.strip()
        words.append(word)

    return words

def make_histogram(s):
    """Make a map from letters to number of times they appear in s.
    s: string
    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist

def print_anagrams(anas):
    for ana in anas.values():
        if len(ana) > 1:
            print ana

def get_anagrams():
    # for each word read in:
    #   create a histogram of the word and sort
    #   get a tuple from the histogram
    #   use histogram as dict key and add word to list for that key
    # TODO: read in words
    words = read_words()
    anas = dict()
    for word in words:
        hist = make_histogram(word)
        h1 = hist.items() # list of tuples
        h1.sort() # sort the list
        key = tuple(h1) # make a tuple of tuples
        anas[key] = anas.get(key, []) + [word]

        #if len(anas[key]) > 2: # ?? for debugging to catch anagrams?
        #    pass

    return anas

def ex_12_04_1():
    anas = get_anagrams()
    print_anagrams(anas)

def order_anagrams_by_word_count(anas):
    o = [] # list?
    for key, val in anas.items(): # add everything to a list of tuples with first tuple element as word count.
        o.append((len(val), key, val))

    o.sort(reverse=True) # order the collection by word count desc

    # now I want to strip out the vals as ordered.
    l = []
    for count, key, val in o:
        l.append(val)

    return l


def ex_12_04_2():
    anas = get_anagrams()
    lanas = order_anagrams_by_word_count(anas)
    for l in lanas:
        print l

def ex_12_05():
    pass

def ex_12_06():
    pass

if __name__ == '__main__':
    #ex_12_01()
    #ex_12_02()
    #ex_12_02()
    #ex_12_03()
    #ex_12_04_1()
    ex_12_04_2()
    #ex_12_05()
    #ex_12_06()
