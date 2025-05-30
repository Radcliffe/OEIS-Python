# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A132199

from itertools import count, islice
from math import gcd
def A132199_gen(): # generator of terms
    a = 7
    for n in count(2):
        yield (b:=gcd(a,n))
        a += b
A132199_list = list(islice(A132199_gen(),20)) # _Chai Wah Wu_, Mar 14 2023

