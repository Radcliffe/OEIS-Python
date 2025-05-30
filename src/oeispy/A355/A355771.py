# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355771

from sympy import divisors
from itertools import count, islice
def c(n): s = str(n); return all(s.count(d)%2 == int(d)%2 for d in set(s))
def f(n): return sum(1 for d in divisors(n, generator=True) if c(d))
def agen():
    n, adict = 1, dict()
    for k in count(1):
        fk = f(k)
        if fk not in adict: adict[fk] = k
        while n in adict: yield adict[n]; n += 1
print(list(islice(agen(), 29))) # _Michael S. Branicky_, Jul 23 2022

