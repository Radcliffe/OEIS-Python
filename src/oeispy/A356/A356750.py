# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356750

from sympy import isprime, factorint
from itertools import count, islice, product
def cond(n): return n&1 and (isprime(n) or len(factorint(n))&1)
def oddpals(): # generator of odd palindromes
    yield from [1, 3, 5, 7, 9]
    for d in count(2):
        for first in "13579":
            for p in product("0123456789", repeat=(d-2)//2):
                left = "".join(p); right = left[::-1]
                for mid in [[""], "0123456789"][d%2]:
                    yield int(first + left + mid + right + first)
def agen(): yield from filter(cond, oddpals())
print(list(islice(agen(), 58))) # _Michael S. Branicky_, Aug 25 2022

