# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A155578

from math import isqrt
def aupto(limit):
    cands = range(1, isqrt(limit)+1)
    left =  set(a**2 +   b**2 for a in cands for b in cands)
    right = set(c**2 + 7*d**2 for c in cands for d in cands)
    return sorted(k for k in left & right if k <= limit)
print(aupto(673)) # _Michael S. Branicky_, Aug 29 2021

