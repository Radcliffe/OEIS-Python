# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A109863

from sympy import isprime
from itertools import product
def tc(n): return 10**len(str(n)) - n
def cond(p): return isprime(p) and isprime(tc(p))
def palcands(digs):
    if digs == 1:   yield from [2, 3, 5, 7]; return
    if digs%2 == 0: yield from [[], [11]][digs==2]; return
    for first in "1379":
        for p in product("0123456789", repeat=(digs-2)//2):
            left = first + "".join(p)
            for mid in "0123456789": yield int(left + mid + left[::-1])
def auptod(digs):
    return [tc(p) for d in range(1, digs+1) for p in palcands(d) if cond(p)]
print(auptod(7)) # _Michael S. Branicky_, Jul 05 2021

