# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A231895

from itertools import accumulate, islice
def A231895_gen(): # generator of terms
    yield 3
    blist = (0,1)
    while True:
        yield blist[-1]+2*(blist := tuple(accumulate(reversed(blist),initial=0)))[-1]
A231895_list = list(islice(A231895_gen(),40)) # _Chai Wah Wu_, Jun 14 2022

