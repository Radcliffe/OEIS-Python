# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A309363

from itertools import count, islice
def A309363gen(): # generator of terms
    b, bdict = 0, {0:(1,)}
    for n in count(2):
        yield b
        if len(l := bdict[b]) > 1:
            b = n-1-l[-2]
        else:
            b = 2
        if b in bdict:
            bdict[b] = (bdict[b][-1],n)
        else:
            bdict[b] = (n,)
A309363_list = list(islice(A309363gen(),20)) # _Chai Wah Wu_, Dec 21 2021

