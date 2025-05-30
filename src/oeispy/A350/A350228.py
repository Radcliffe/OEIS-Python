# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350228

from itertools import islice, count
def A350228gen():
    yield from (1,0)
    b, bdict = 0, {1:(1,),0:(2,)}
    for n in count(3):
        if len(l := bdict[b]) > 1:
            m = (n-1-l[-2])*b
            if m in bdict:
                bdict[m] = (bdict[m][-1],n)
            else:
                bdict[m] = (n,)
            b = m
        else:
            bdict[1] = (bdict[1][-1],n)
            b = 1
        yield b
A350228_list = list(islice(A350228gen(),20)) # _Chai Wah Wu_, Dec 21 2021

