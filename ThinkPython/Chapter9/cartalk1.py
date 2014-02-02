def is_pair(s, debug=False):
    if debug: print "checking: [{0}]".format(s),
    if len(s) < 2:
        return False
    return s[0] == s[1]

def has_3_consecutive_pairs(word, debug=False):
    if len(word) < 6:
        return False
    if debug: print "Word:", word

    i = 0
    j = 6
    while j <= len(word):
        letters = word[i:j]
        if debug: print "examining: {0}".format(letters)
        if is_pair(letters[0:2]) and is_pair(letters[2:4]) and is_pair(letters[4:]):
            return True
        if debug: print ''
        i += 1
        j += 1

    return False

if __name__ == '__main__':
    count = 0
    indicator = 1
    fin = open('words.txt') 
    for line in fin: 
        word = line.strip()
        indicator += 1
        if indicator % 100 == 0:
            print '.',

        if has_3_consecutive_pairs(word):
            print word
            count += 1

        if indicator % 80000 == 0:
            raw_input("pause to check")

    print count, "words have 3 consecutive pairs"
