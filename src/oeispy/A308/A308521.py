# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A308521

from itertools import count, islice, accumulate
def A308521_gen(): # generator of terms
    blist, m = tuple(), 1
    for i in count(1):
        yield (blist := tuple(accumulate(reversed(blist),initial=m)))[-1]
        m *= 2*i
A308521_list = list(islice(A308521_gen(),30)) # _Chai Wah Wu_, Jun 11 2022

