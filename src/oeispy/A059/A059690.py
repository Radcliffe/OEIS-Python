# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A059690

from itertools import count, islice
from sympy import isprime, primerange
def c(p): return not isprime((p-1)//2) and isprime(2*p+1)
def agen():
    s = 1
    for n in count(2):
        yield s; s += sum(1 for p in primerange(2**(n-1)+1, 2**n) if c(p))
print(list(islice(agen(), 20))) # _Michael S. Branicky_, Oct 09 2022

