# Vernam cipher

import random

def randomKey(l):
    """ 
    Function that generates a random key.
    Length of the key depends on the parameter l.
    """
    res = ""
    for i in range(l):
        tmp = random.randint(ord('A'), ord('Z'))
        res += chr(tmp)
    return res

def rotChar(c, k):
    """ 
    Function that applies the letter shift.
    c is a char
    k is an int
    """ 
    if not c.isalpha():
        return c

    if c.isupper():
        r = 'A'
    else:
        r = 'a'

    alpha_val = ord(c) % ord(r)
    alpha_val = (alpha_val + k) % 26
    return chr(ord(r) + alpha_val)

def vernam(s, k):
    """ 
    Function that applies Vernam's cipher
    """ 
    l = len(s)
    res = ""
    for i in range(l):
        res += rotChar(s[i], ord(k[i]))
    return res

def decVernam(s, k):
    """ 
    Function that decodes Vernam cipher
    """ 
    l = len(s)
    res = ""
    for i in range(l):
        res += rotChar(s[i], -ord(k[i]))
    return res

#  Tests

m = "Hello, this is a test !"
k = randomKey(len(m))
e = vernam(m, k)
c = decVernam(e, k)

print(m)
print(k)
print(e)
print(c)