# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A162354

from sympy import primerange
from itertools import count, takewhile
def hash(n): return "".join(sorted(str(n)))
def aupto_digits(d):
    tris   = takewhile(lambda x:x<10**d, (i*(i+1)//2 for i in count(0)))
    primes = primerange(1, 10**d)
    T = set(map(hash, tris))
    return [p for p in primes if hash(p) in T]
print(aupto_digits(4)) # _Michael S. Branicky_, Feb 18 2024

