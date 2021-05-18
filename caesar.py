# Caesar cipher

def charCaesar(c, k):
    """
    Function that applies the Caesar cipher
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

def strCaesar(s, k):
    """
    Function that applies Caesar cipher to a string
    """
    res = ""
    for l in s:
        res += charCaesar(l, k)
    return res

def bruteCaesar(s):
    """ 
    Function that uses brute force to break Caesar cipher
    """ 
    for i in range(26):
        print(strCaesar(s, i))

def freqChar(s):
    """ 
    Function that build an histogram of the letters' frequency
    of a string
    """ 
    l = []
    for i in range(26):
        l.append(0)

    for c in s:
        if c.isalpha():
            tmp = ord(c.upper()) - ord('A')
            print(tmp)
            l[tmp] += 1
    return l

def max(l):
    """ 
    Function that returns the maximum of a list
    """ 
    max = 0
    for i in range(26):
        if l[i] > l[max]:
            max = i
    return max

def caesarKey(s):
    """ 
    Function that finds the key to break the Caesar cipher,
    thanks to a histogram.
    Considers that the most present letter in texts is 'e'
    """ 
    l = freqChar(s)
    m = max(l)
    return abs(m - 4)

def caesarKey2(s):
    """ 
    Function that finds the key to break the Caesar cipher,
    thanks to a histogram.
    Considers that the most present letter in texts is 'e'
    """ 
    l = freqChar(s)
    m = max(l)
    return m

def anaFreqCaesar(s):
    """ 
    Function that breaks Caesar cipher
    """ 
    key = caesarKey(s)
    return strCaesar(s, -key)




# Tests

print(charCaesar('a', -5))
print(strCaesar("Hello World !", 10))
bruteCaesar('Rovvy Gybvn !')

s = "Sqdmxf pq Duh qef gz bqdeazzmsq qfdmzsq, gzq nulmddqduq pq xm zmfgdq, gz ygfmzf cgu, sdmoq m xm ymsuq qf m gz xazs qzfdmuzqyqzf, ymue mgeeu sdmoq m gz ykefqduqgj qxujud, qef pqhqzg gz yqgdfduqd bmdrmuf. Eqe otqhqgj nxmzoe, eqe kqgj zkofmxabqe qf eaz ymzfqmg zaud qrrdmkqzf qf rmeouzqzf. Ux bmdoagdf pqe oazfdqqe buffadqecgqe qz smszmzf em huq oayyq otmeeqgd pq yazefdqe. Qz oqe fqybe aneogde, asdqe, sagxqe qf hmybudqe bgxxgxqzf, qf xqe ymsuouqze eazf pqe ymzubgxmfqgde qjbqdfe. Oazfdq oqe yqzmoqe, ux rmgf gz fgqgd m smsqe m xm tmgfqgd. Omd Sqdmxf qef bxge cg’gz sgqdduqd ag gz ymsq. O’qef gz Eadoqxqgd. Ux qef gzucgq. Mg oagde pq eqe mhqzfgdqe, ux dqzoazfdqdm gzq mgfadufmudq ymue sqzqdqgeq bdqfdqeeq, gz fdagnmpagd bmuxxmdp mg sdmzp oaqgd, qf gzq ymsuouqzzq ombduouqgeq mgj otmdyqe hqzqzqgj. Myue p’gz vagd, myagde p'gzq zguf. Ymue mg nagf pq em cgqfq, bqgf-qfdq bagddm-f-ux bdazazoqd eaz pqdzuqd haqg : dqfdaghqd eaz tgymzufq bqdpgq…"

print(caesarKey(s))
print(anaFreqCaesar(s))