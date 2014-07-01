import collections
import string
import random

def shift(prefix, word):
    return prefix[1:] + (word,)

def get_prefix(q):
    prefwords = list(q)
    prefix = ""
    for w in prefwords:
        prefix += w + " "

    prefix = prefix.strip(string.whitespace)
    return prefix

def markov_analyse_file(file, prefixLen=2):
    fin = open(file)

    words = dict()
    #q = collections.deque()
    header_read = False
    prefix = ()
    for line in fin:

        if not header_read:
            if  "START OF THIS PROJECT GUTENBERG EBOOK" in line:
                header_read = True
            continue

        if "END OF THIS PROJECT GUTENBERG EBOOK" in line:
            break

        line = line.replace('_', ' ')
        line = line.replace('-', ' ')
        #line = line.replace('://', ' ')
        line_words = line.split()

        if "CHAPTER" in line or "VOLUME" in line:
            continue

        for word in line_words:
            # strip out web urls
            if "://" in word:
                continue

            word = word.translate(None, string.punctuation)
            word = word.strip(string.punctuation)
            if word.isalpha():
                word = word.lower()

                # do we have any previous words for a prefix?
                if len(prefix) < prefixLen:
                    prefix += (word,)
                    continue

                # 1. we do have a prefix, get the prefix
                #prefix = get_prefix(q)
                # 2. add current word to list of suffixes for the prefix
                #suffixes = words.get(prefix)
                #if suffixes is None:
                #    suffixes = [word]
                #else:
                #    if not word in suffixes:
                #        suffixes.append(word)

                #words[prefix] = suffixes
                
                # update the q od porefix words
                #q.append(word)
                #if (len(q) > prefixLen):
                #    q.popleft()

                try:
                    words[prefix].append(word)
                except KeyError:
                    # if there is no entry for this prefix, make one
                    words[prefix] = [word]

                prefix = shift(prefix, word)

    return words

def generate_random_text(markov, wordcount = 50):
    # get the start
    prefix = random.choice(markov.keys())

    for i in range(wordcount):
        suffixes = markov.get(prefix, None)
        if suffixes == None:
            generate_random_text(markov, wordcount - i)
            return

        suffix = random.choice(suffixes)
        print suffix,

        #key = collections.deque(prefix.split())
        #key.popleft()
        #key.append(suffix)

        #prefix = get_prefix(key)
        prefix = shift(prefix, suffix)
    

if __name__ == '__main__':
    words = markov_analyse_file("books\Bradley_TheColorsOfSpace.txt", 2)
    generate_random_text(words, 50)
    print
