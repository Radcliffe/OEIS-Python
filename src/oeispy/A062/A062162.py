# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A062162

from itertools import islice, accumulate
def A062162_gen(): # generator of terms
    blist, m = tuple(), -1
    while True:
        yield (blist := tuple(accumulate(reversed(blist),initial=(m:=-m))))[-1]
A062162_list = list(islice(A062162_gen(),20)) # _Chai Wah Wu_, Jun 10 2022

