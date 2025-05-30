# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A369203

from collections import Counter
from sympy import primeomega as W
from sympy.utilities.iterables import multiset_permutations as MP
from itertools import combinations_with_replacement, count, islice
def counteq(n):
    c = Counter(W(int("".join(p))) for p in MP(str(n)) if p[0]!='0')
    return [i for i in c if c[i] == i]
def agen(): # generator of terms
    adict, n = dict(), 1
    for d in count(len(str(2**n))):
        for f in "123456789":
            for r in combinations_with_replacement("0123456789", d-1):
                k = int(f+"".join(r))
                for v in counteq(k):
                    if v not in adict:
                        adict[v] = k
                while n in adict: yield adict[n]; n += 1
print(list(islice(agen(), 8))) # _Michael S. Branicky_, Jan 16 2024

