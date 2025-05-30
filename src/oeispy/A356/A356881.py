# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356881

from sympy import isprime
from itertools import product
def ispal(n): s = str(n); return s == s[::-1]
def oddpals(d): # generator of odd palindromes with d digits
    if d == 1: yield from [1, 3, 5, 7, 9]; return
    for first in "13579":
        for p in product("0123456789", repeat=(d-2)//2):
            left = "".join(p); right = left[::-1]
            for mid in [[""], "0123456789"][d%2]:
                yield int(first + left + mid + right + first)
def auptod(dd):
    N, alst, pp, once, twice = 10**dd, [], [2, 3, 5, 7, 11], set(), set()
    pp += [p for d in range(3, dd+1, 2) for p in oddpals(d) if isprime(p)]
    sums = (p+q for p in pp for q in pp if p<=q and p+q<N and ispal(p+q))
    for s in sums:
        if s in once: twice.add(s)
        else: once.add(s)
    return sorted(twice)
print(auptod(5)) # _Michael S. Branicky_, Sep 02 2022

