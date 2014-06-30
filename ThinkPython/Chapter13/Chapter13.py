import string
import random

from TPCommon import *

def count_total_words(words):
    total = 0
    for word, count in words.items():
        total += count
    
    print total, "words used"



def count_different_words(words):
    print len(words), "different words used"
    
def print_most_frequent(words, count):
    freq = zip(words.values(), words.keys())
    freq.sort(reverse=True)

    counter = 0;
    for num, word in freq:
        print word, "occurs", num, "times"
        counter += 1
        if counter >= count:
            break

def analyse_book(file):
    words = read_gutenberg_book(file)
    count_total_words(words)
    count_different_words(words)
    # ex 13.3
    #print_most_frequent(words, 20)

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


def choose_from_hist():

    pass

def get_histogram(s):
    s = s.translate(None, string.whitespace)
    s = s.lower()
    return make_histogram(s)

def ex_13_5():
    hist = get_histogram("Make a map from letters to number of times they appear in s")
    print hist
    #TODO select letters from hist chosen with probability in proportion to frequency.

    


if __name__ == '__main__':
    #print string.whitespace
    #print string.punctuation

    #words = read_words_file()
    #print len(words), " word read"
    #words = read_words_from_file("TestRead.txt")
    #print words
    #ex_13_2()
    ex_13_5()

