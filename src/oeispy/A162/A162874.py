# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A162874

from sympy import nextprime, factorint
def cubefree(n): return max(e for e in factorint(n).values()) <= 2
def auptop(limit):
    alst, p, r = [], 3, 5
    while p < limit:
        if r - p == 2 and not any(cubefree(i) for i in [p-1, p+1, r+1]):
            alst.extend([p, r])
        p, r = r, nextprime(p)
    return alst
print(auptop(2*10**6)) # _Michael S. Branicky_, Aug 22 2021

