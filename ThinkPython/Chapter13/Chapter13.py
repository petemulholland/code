import string
import random

from TPCommon import *

def count_total_words(words):
    return sum(words.values())

def count_different_words(words):
    return len(words)
    
def print_most_frequent(words, count):
    freq = zip(words.values(), words.keys())
    freq.sort(reverse=True)

    counter = 0;
    for num, word in freq:
        print word, "occurs", num, "times"
        counter += 1
        if counter >= count:
            break

def analyse_book(file, num=0):
    words = read_gutenberg_book(file)
    print count_total_words(words),  "words used"
    print count_different_words(words), "different words used"
    # ex 13.3
    if num > 0:
        print_most_frequent(words, num)

def ex_13_2():
    # todo: download several books, create a list of names and run them through
    print "Analysing Lovecraft Shunned House"
    analyse_book("Books\LovecraftShunnedHouse.txt")
    
    print "Analysing Coppel Turning Point"
    analyse_book("Books\Coppel_TurningPoint.txt")
    
    print "Analysing Beck Vanishing Point"
    analyse_book("Books\Beck_VanishingPoint.txt")
    
    print "Analysing Dick Mr Spaceship"
    analyse_book("Books\Dick_MrSpaceship.txt")

    print "Analysing Bradley The Colors Of Space"
    analyse_book("Books\Bradley_TheColorsOfSpace.txt")

    print "Analysing Bradley Door Through Space"
    analyse_book("Books\Bradley_DoorThroughSpace.txt")

def print_book_words_not_in_dict(dictwords, bookwords):
    missingwords = []
    for word in bookwords.keys():
        if not word in dictwords:
            missingwords.append(word)

    missingwords.sort()
    print len(missingwords), "words found that are not in the dictionary"
    print "missing words:"
    for word in missingwords:
        print word

def ex_13_4():
    dictwords = read_words_file()
    bookwords = read_gutenberg_book("Books\Bradley_TheColorsOfSpace.txt")
    print_book_words_not_in_dict(dictwords, bookwords)


def choose_from_hist(hist):
    # 
    vals = []
    for word, freq in hist.items():
        vals.extend([word] * freq)

    #return vals[random.randint(0, len(vals) - 1)]
    return random.choice(vals)

def get_histogram(s):
    s = s.translate(None, string.whitespace)
    s = s.lower()
    return make_histogram(s)

def ex_13_5a():
    hist = make_histogram("aab")
    vals = {}
    for x in range(0, 15):
        val = choose_from_hist(hist)
        vals[val] = vals.get(val, 0) + 1
    
    print vals

def ex_13_5():
    a_string = "Make a map from letters to number of times they appear in s"
    hist = get_histogram(a_string)
    print hist
    #TODO select letters from hist chosen with probability in proportion to frequency.
    ln = len(a_string.translate(None, string.whitespace))

    vals = {}
    for x in range(0, ln):
        val = choose_from_hist(hist)
        vals[val] = vals.get(val, 0) + 1
    
    print vals

def emma():
    print "Analysing emma"
    analyse_book("Books\emma.txt", 0)

`    #print string.whitespace
    #print string.punctuation

    #words = read_words_file()
    #print len(words), " word read"
    #words = read_words_from_file("TestRead.txt")
    #print words
    #ex_13_2()
    ex_13_5()
    #emma()

