# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A062970

from itertools import count, accumulate, islice
def A062970_gen(): # generator of terms
    yield from accumulate((k**k for k in count(1)),initial=1)
A062970_list = list(islice(A062970_gen(),20)) # _Chai Wah Wu_, Jun 17 2022

