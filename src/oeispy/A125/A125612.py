# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A125612

from itertools import count
from sympy import nthroot_mod, isprime
def A125612(n):
    m = 11**n
    r = sorted(nthroot_mod(1,10,m,all_roots=True))
    for i in count(0,m):
        for p in r:
            if isprime(i+p): return i+p # _Chai Wah Wu_, May 02 2024

