# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370849

from sympy import factorint
from itertools import combinations
from sympy.utilities.iterables import multiset_permutations
def a(n):
    m = (int('9'*n),)*2
    for c in combinations("123456789", 2):
        for r in multiset_permutations(c[0]*n+c[1]*n, n):
            t = int("".join(r))
            s = max(factorint(t, limit=m[0]))
            m = min(m, (s, t))
    return m[1]
print([a(n) for n in range(2, 12)]) # _Michael S. Branicky_, Mar 03 2024

