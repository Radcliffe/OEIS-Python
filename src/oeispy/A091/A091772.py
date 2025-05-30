# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A091772

from itertools import count, accumulate, islice
def A091772_gen(): # generator of terms
    yield 1
    blist, b, c = (1,2), 1, 1
    for n in count(1):
        blist = list(accumulate(blist, initial=(b:=blist[-1])))
        yield gcd(b, c := c*(4*n+2)//(n+2))
A091772_list = list(islice(A091772_gen(),20)) # _Chai Wah Wu_, Jun 22 2022

