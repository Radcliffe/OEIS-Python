# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A069870

from collections import Counter
from sympy.utilities.iterables import partitions, multiset_permutations
from sympy import isprime
def A069870(n):
    d = 10**n
    smin, m = n+1, d
    if n==3 or n%3:
        for s in range(1,n+1):
            if s>smin:
                break
            m = min((k for k in (int(''.join(str(d) for d in a)) for p in partitions(n,m=s) for a in multiset_permutations(Counter(p).elements())) if isprime(k)),default=d)
            if m<d:
                smin=s
    if m == d:
        return 0
    else:
        return m # _Chai Wah Wu_, Feb 21 2024

