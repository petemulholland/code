# exercise 11-2
def histogram(s):
    d = dict() 
    for c in s: 
        d[c] = d.get(c, 0) + 1
        
    return d


# exercise 11-3
def print_hist(h): 
    for c in sorted(h.keys()): 
        print c, h[ c]


# exercise 11-4
def reverse_lookup(d, v): 
    keys = []
    for k in d: 
        if d[k] == v: 
            keys.append(k)

    return keys

# exercise 11-5
def invert_dict(d): 
    inverse = dict() 
    for key in d: 
        val = d[key] 
        inverse.setdefault(val, []).append(key)
      
    return inverse

# exercise 11-6
def ex_11_6():
    pass

# exercise 11-7
def ex_11_7():
    pass

# exercise 11-X
def ex_11_x():
    pass


if __name__ == '__main__':
    #print histogram('brontosaurus')
    #print_hist(histogram('brontosaurus'))
    hist = histogram('brontosaurus')
    print reverse_lookup(hist, 2)
    inv = invert_dict(hist)
    print inv
