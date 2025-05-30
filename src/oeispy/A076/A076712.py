# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A076712

from itertools import count, islice
def A076712_gen(): # generator of terms
    for n in count(1):
        m = t = n*(n+1)>>1
        while m not in {1,37,58,89,145,42,20,4,16}:
            m = sum((0, 1, 4, 9, 16, 25, 36, 49, 64, 81)[ord(d)-48] for d in str(m))
        if m == 1:
            yield t
A076712_list = list(islice(A076712_gen(),20)) # _Chai Wah Wu_, Aug 02 2023

