# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A076612

from itertools import chain, count, islice
def A076612_gen(): # generator of terms
    return chain((1,4,6,8,9),chain.from_iterable((int((s:=str(d))+e+s[::-1]) for d in range(10**l,10**(l+1)) for e in '014689') for l in count(0)))
A076612_list = list(islice(A076612_gen(),20)) # _Chai Wah Wu_, Jun 23 2022

