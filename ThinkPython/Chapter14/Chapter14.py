import os
import shelve

from anagram_sets import *

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print path
        else:
            walk(path)

def sed(pattern, replacement, fileIn, fileOut):
    try: 
        pathIn = os.path.join(os.getcwd(), fileIn)
        pathOut = os.path.join(os.getcwd(), fileOut)
        fin = open(pathIn)
        fout = open(pathOut, 'w')
        for line in fin:
            fout.write(line.replace(pattern, replacement))

        fin.close()
        fout.close()
    except IOError, Argument:
        print 'An error occurred', Argument

def ex_14_2():
    sed('the', 'rgw', 'ex_14_2_in.txt', 'ex_14_2_out.txt')
    sed('the', 'rgw', 'ex_14_2_not_there.txt', 'ex_14_2_out.txt')

def shelve_anas(filename, anas):
    shelf = shelve.open(filename, 'c')
    for word, ana_list in anas.iteritems():
        shelf[word] = ana_list

    shelf.close()

def unshelve_anas(filename, word):
    shelf = shelve.open(filename);
    sig = signature(word) # not sure what this is about!

    try: 
        return shelf[sig]
    except KeyError:
        return []
    pass

def ex_14_3():
    # TODO: get_anagrams not returning what I want.
    anas = all_anagrams('..\words.txt')
    shelve_anas('anagrams.db', anas)
    spots = unshelve_anas('anagrams.db', 'spot')
    print spots

if __name__ == '__main__':
    #walk(os.path.abspath(os.path.join(os.getcwd(), "..")))
    #ex_14_2()
    ex_14_3()