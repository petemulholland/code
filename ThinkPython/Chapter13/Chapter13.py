import string
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
    print_most_frequent(words, 20)

def ex_13_2():
    # todo: downlaod several books, create a list of names and run them through
    analyse_book("LovecraftShunnedHouse.txt")

if __name__ == '__main__':
    #print string.whitespace
    #print string.punctuation

    #words = read_words_file()
    #print len(words), " word read"
    #words = read_words_from_file("TestRead.txt")
    #print words
    ex_13_2()

