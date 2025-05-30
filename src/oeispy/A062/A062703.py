# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A062703

from itertools import count, islice
from sympy import nextprime, prevprime
def agen(): # generator of terms
    for k in count(4, step=2):
        kk = k*k
        if prevprime(kk//2+1) + nextprime(kk//2-1) == kk:
            yield kk
print(list(islice(agen(), 37))) # _Michael S. Branicky_, May 24 2022

