# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A249155

from gmpy2 import digits
def palQ(n, b): # check if n is a palindrome in base b
    s = digits(n, b)
    return s == s[::-1]
def palQgen(l, b): # generator of palindromes in base b of length <= 2*l
    if l > 0:
        yield 0
        for x in range(1, l+1):
            for y in range(b**(x-1), b**x):
                s = digits(y, b)
                yield int(s+s[-2::-1], b)
            for y in range(b**(x-1), b**x):
                s = digits(y, b)
                yield int(s+s[::-1], b)
A249155_list = [n for n in palQgen(8, 6) if palQ(n, 15)] # _Chai Wah Wu_, Nov 29 2014

