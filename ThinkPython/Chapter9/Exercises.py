def exercise91():
    fin = open('words.txt') 
    for line in fin: 
        word = line.strip() 
        if len(word) > 20:
            print word

def has_no_e(word):
    return not 'e' in word and not 'E' in word


def exercise92():
    fin = open('words.txt') 
    word_count = 0
    no_e_count = 0
    for line in fin: 
        word = line.strip()
        word_count += 1
        if has_no_e(word):
            print word
            no_e_count += 1


    print "percentage of words with no e:", no_e_count * 100.0 / word_count

def avoids(word, excluded):
    for letter in excluded:
        if letter in word:
            return False

    return True


def exercise93():
    avoid = raw_input("enter 5 letters to avoid [j,q,x,y andk are least commonly used] :")

    fin = open('words.txt') 
    avoids_count = 0
    for line in fin: 
        word = line.strip()
        if avoids(word, avoid):
            #print word
            avoids_count += 1


    print "Count of words that do not contain these letters: '", avoid, "' - ", avoids_count

def uses_only(word, letters):
    for letter in word:
        if not letter in letters:
            return False
    return True

def exercise94():
    include = raw_input("enter letters to only be used in each word:")

    fin = open('words.txt') 
    for line in fin: 
        word = line.strip()
        if uses_only(word, include):
            print word

def uses_all(word, letters):
    result = True
    for letter in letters:
        result = result and letter in word

    return result

def exercise95():
    use_all = raw_input("enter letters that each word must use:")

    count = 0
    fin = open('words.txt') 
    for line in fin: 
        word = line.strip()
        if uses_all(word, use_all):
            print word
            count += 1

    print count, "words use all letters", use_all

def is_abecedarian(word):
    last = word[:1]
    for letter in word[1:]:
        if letter < last:
            return False
        last = letter

    return True

def exercise96():
    count = 0
    fin = open('words.txt') 
    for line in fin: 
        word = line.strip()
        if is_abecedarian(word):
            print word
            count += 1

    print count, "words are abecedarian"


if __name__ == '__main__':
    exercise96()
