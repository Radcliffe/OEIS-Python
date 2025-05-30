# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A347008

from sympy import primerange
from collections import Counter
def aupto(limit):
    primes = list(primerange(2, limit//3+1))
    nums = [p*q+p+q for i, p in enumerate(primes) for q in primes[i+1:]]
    counts = Counter([k for k in nums if k <= limit])
    return sorted(k for k in counts if counts[k] == 2)
print(aupto(2604)) # _Michael S. Branicky_, Aug 10 2021

