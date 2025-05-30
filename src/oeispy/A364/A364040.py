# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364040

from sympy import primeomega
from itertools import count, islice, permutations as P
def agen(): # generator of terms
    adict, n = dict(), 0
    D = [p for d in range(1, 11) for p in P("0123456789", d) if p[0] != "0"]
    for k in (int("".join(t)) for t in D):
        v = primeomega(k)
        if v not in adict:
            adict[v] = k
            while n in adict: yield adict[n]; n += 1
    yield from (adict[n] if n in adict else -1 for n in count(n))
print(list(islice(agen(), 22))) # _Michael S. Branicky_, Apr 05 2024

