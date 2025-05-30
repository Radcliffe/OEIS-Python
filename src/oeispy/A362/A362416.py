# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362416

from functools import lru_cache
from sympy import factorint, isprime
@lru_cache(maxsize=None)
def winning(q):
    if q == 1: return True
    if isprime(q): return False
    pf = factorint(q)
    if winning(q+1) or any(winning(q//p) for p in pf):
        return False
    if not winning(q+1) and all(not winning(q//p) for p in pf):
        return True
print([k for k in range(1, 200) if winning(k)]) # _Michael S. Branicky_, Apr 20 2023

