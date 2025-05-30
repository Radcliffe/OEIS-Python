# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A262069

def palgen(l,b=10): # generator of palindromes in base b of length <= 2*l
    if l > 0:
        yield 0
        for x in range(1,l+1):
            n = b**(x-1)
            n2 = n*b
            for y in range(n,n2):
                k, m = y//b, 0
                while k >= b:
                    k, r = divmod(k,b)
                    m = b*m + r
                yield y*n + b*m + k
            for y in range(n,n2):
                k, m = y, 0
                while k >= b:
                    k, r = divmod(k,b)
                    m = b*m + r
                yield y*n2 + b*m + k
A262069_list = [n for n in palgen(5,60) if str(n) == str(n)[::-1]] # _Chai Wah Wu_, Sep 10 2015

