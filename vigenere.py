# Vigenere cipher

def charVig(c, k):
    """
    Function that applies the Vigenere cipher
    on one char
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

def vigenere(s, k):
    """ 
    Function that applies the Vigenere cipher 
    on the whole message
    """ 
    le = len(k)
    i=0
    res = ""
    for l in s:
        i = i % le
        res += charVig(l, ord(k[i].upper()) % ord('A'))
        i+=1
    return res

def decVigenere(s, k):
    """ 
    Function that allows to decrypt a message ciphered with
    Vigenere
    """ 
    le = len(k)
    i=0
    res = ""
    for l in s:
        index = i % le
        res += charVig(l, -(ord(k[index].upper()) % ord('A')))
        i+=1
    return res

# Breaking Vigenere



# Some tests
s = vigenere("Hello !", "test")
print(s)
print(decVigenere(s, "test"))