import string

def get_words_from_line(line, words):
    #line = line.replace('.', ' ')
    line = line.replace('_', ' ')
    line = line.replace('-', ' ')
    #line = line.replace('://', ' ')
    line_words = line.split()
    for word in line_words:
        if "://" in word:
            continue

        word = word.translate(None, string.punctuation)
        word = word.strip(string.punctuation)
        if word.isalpha():
            word = word.lower()
            words[word] = words.get(word, 0) + 1

def read_gutenberg_book(file):
    fin = open(file)
    words = dict()
    header_read = False

    for line in fin:
        if not header_read:
            if  "START OF THIS PROJECT GUTENBERG EBOOK" in line:
                header_read = True

            continue

        if "END OF THIS PROJECT GUTENBERG EBOOK" in line:
            break

        get_words_from_line(line, words)

    return words

def read_words_from_file(file):
    fin = open(file)
    words = dict()
    for line in fin:
        get_words_from_line(line, words)

    return words


def read_words_file():
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

