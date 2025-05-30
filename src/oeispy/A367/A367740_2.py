# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367740

from itertools import product, count, islice
def A367740_gen(): # generator of terms
    yield from (-1,0,0)
    for l in count(1):
        m = 10**(l+1)
        for d in product('0123456789',repeat=l):
            for a, b, c in ((1, 0, 0), (1, 1, 0), (1, 4, 2), (1, 5, 5), (1, 7, 5)):
                k = a*m+int(s:=''.join(d))*10+b
                r = b*m+int(s[::-1])*10+a
                if c*(k+1)==r-1:
                    yield c
            a,b = 1,9
            k = a*m+int(s:=''.join(d))*10+b
            r = b*m+int(s[::-1])*10+a
            p,q = divmod(r-1,k+1)
            if not q:
                yield p
        a,b,c=2,6,3
        for d in product('0123456789',repeat=l):
            k = a*m+int(s:=''.join(d))*10+b
            r = b*m+int(s[::-1])*10+a
            if c*(k+1)==r-1:
                yield c
A367740_list = list(islice(A367740_gen(),20)) # _Chai Wah Wu_, Dec 01 2023

