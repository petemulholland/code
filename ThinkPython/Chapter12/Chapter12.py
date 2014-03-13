import random

def sumall(*args):
    sum = 0
    for num in args:
        sum += num

    return sum

def ex12_1():
    print "sumall(1, 2) returns", sumall(1, 2)
    print "sumall(3, 4) returns", sumall(3, 4)
    print "sumall(4, 5, 6) returns", sumall(4, 5, 6)
    print "sumall(7, 8, 9, 10) returns", sumall(7, 8, 9, 10)


def sort_by_length_random(words):
    """Sort a list of words in reverse order by length.

    This is the solution to the exercise.  It is unstable in the
    sense that if two words have the same length, their order in
    the output list is random.

    It works by extending the list of tuples with a column of
    random numbers; when there is a tie in the first column,
    the random column determines the output order.

    words: list of strings

    Returns: list of strings
    """
    t = []
    for word in words:
       t.append((len(word), random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, _, word in t:
        res.append(word)
    return res

def ex12_2():
    words = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

    t = sort_by_length_random(words)
    for x in t:
        print x

def most_frequent(s):
    letters = sorted(s.lower())
    t = []
    #b = []
    lastLetter = ''
    count = 0
    for l in letters:
        if l == lastLetter:
            count += 1
        else:
            if lastLetter.isalpha():
                t.append((count, lastLetter))
                #b.append((lastLetter, count))

            lastLetter = l
            count = 1

    t.append((count, lastLetter))
    #b.append((lastLetter, count))

    # should have a dict of letters & counts
    # need to sort them
    t.sort(reverse=True)
    #b.sort()
    print t
    #print b
    for count, l in t:
        print l, 
    
    print

    pass

def ex12_3():
    """
    Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. 
    Find text samples from several different languages and see how letter frequency varies between languages. 
    Compare your results with the tables at http:// en.wikipedia.org/ wiki/ Letter_frequencies . 
    Solution: http:// thinkpython.com/ code/ most_frequent.py .
    """
    most_frequent("The quick brown fox jumps over the lazy dog")

    most_frequent("""Letter frequencies, like word frequencies, tend to vary, both by writer and by subject. One cannot write an essay about x-rays without using frequent Xs, 
                     and the essay will have an idiosyncratic letter frequency if the essay is about the frequent use of x-rays to treat zebras in Qatar. 
                     Different authors have habits which can be reflected in their use of letters. Hemingway's writing style, for example, is visibly different from Faulkner's. 
                     Letter, bigram, trigram, word frequencies, word length, and sentence length can be calculated for specific authors, and used to prove or disprove authorship of texts, 
                     even for authors whose styles are not so divergent.
                     Accurate average letter frequencies can only be gleaned by analyzing a large amount of representative text. With the availability of modern computing and 
                     collections of large text corpora, such calculations are easily made. Examples can be drawn from a variety of sources (press reporting, religious texts, 
                     scientific texst and general fiction) and there are differences especially for general fiction with the position of 'h' and 'i', with H becoming more common.""")

    pass

def ex12_4():
    pass

def ex12_5():
    pass

def ex12_6():
    pass

def main():
    pass


if __name__ == '__main__':
    #ex12_1()
    #ex12_2()
    ex12_3()
