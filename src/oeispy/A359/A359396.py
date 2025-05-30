# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A359396

from sympy import isprime
from itertools import count, islice
def f(k):
    j = 1
    while isprime(k**j + 2): j += 1
    return j-1
def agen():
    adict, n = dict(), 1
    for k in count(2):
        v = f(k)
        if v not in adict: adict[v] = k
        while n in adict: yield adict[n]; n += 1
print(list(islice(agen(), 5))) # _Michael S. Branicky_, Jan 09 2023

