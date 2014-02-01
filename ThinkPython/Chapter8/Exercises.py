# exercise 8-4
def find(word, letter, start=0): 
    index = start 
    while index < len(word): 
        if word[index] == letter: 
            return index 
        index = index + 1 
    
    return -1


# exercise 8-5
def count(word, to_find):
    count = 0 
    for letter in word: 
        if letter == to_find: 
            count = count + 1 
        
    return count


# exercise 8-6
def count(word, to_find):
    count = 0
    idx = 0
    while  idx >= 0 and idx < len(word):
        idx = find(word, to_find, idx)
        if idx >= 0:
            count += 1
            idx += 1

    return count

# exercise 8-9
def is_reverse( word1, word2): 
    if len(word1) != len(word2): 
        return False 
    i = 0 
    j = len(word2) - 1
    while j >= 0: 
        if word1[i] != word2[j]: 
            return False 
        i += 1
        j -= 1 
        
    return True

# exercise 8-10
def is_palindrome(word):
    return word == word[::-1]


# exercise 8-11
def any_lowercase1(s): 
    for c in s: 
        if c.islower():
            return True 
    return False 
        
def any_lowercase4(s): 
    flag = False 
    for c in s: 
        flag = flag or c.islower() 
    return flag 
     
def any_lowercase5(s): 
    for c in s: 
        if c.islower(): 
            return True 
        
    return False

 
# exercise 8-12
def rotate_word(s, n):
    start = 0

    result = ''
    for c in s:
        if not c.isalpha():
            print c, " is not an alpha char"
            break

        if c.isupper():
            start = ord('A')
        else:
            start = ord('a')

        i = ord(c) - start
        result += chr((i + n) % 26 + start)

    return result

word = 'banana'

