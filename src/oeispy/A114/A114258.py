# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A114258

from math import isqrt
from itertools import count, islice
def A114258_gen(): # generator of terms
    for l in count(1):
        a = isqrt(10**((l<<1)-1))
        if (a9:=a%9):
            a -= a9
        for b in range(a,10**l,9):
            for c in (0,2):
                k = b+c
                if sorted(str(k)*2)==sorted(str(k**2)):
                    yield k
A114258_list = list(islice(A114258_gen(),20)) # _Chai Wah Wu_, Feb 27 2024

