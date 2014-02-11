import pronounce

def read_words():
    """Read the words in words.txt and return a dictionary
    that contains the words as keys"""
    words = []
    fin = open('..\words.txt')
    for line in fin:
        word = line.strip().lower()
        words.append(word)

    return words

def check_homophones(word, pron):
    if len(word) < 4:
        return

    if word not in pron:
        return
    wpron = pron[word]

    hom1 = word[1:]
    if hom1 not in pron:
        return
    h1pron = pron[hom1]

    hom2 = word[0] + word[2:]
    if hom2 not in pron:
        return
    h2pron = pron[hom2]

    if wpron == h1pron and wpron == h2pron:
        print word, hom1, hom2


def main():
    words = read_words()
    pron = pronounce.read_dictionary()

    for word in words:
        check_homophones(word, pron)

if __name__ == '__main__':
    main()