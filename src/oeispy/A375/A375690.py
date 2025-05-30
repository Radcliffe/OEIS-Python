# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375690

from sympy import isprime
from itertools import product
def agen(): # generator of terms
    an, s = 3, "3"
    while an > 0:
        yield an
        an = -1
        for f, r in product("1379", "0123456789"):
            sn = f+r+s+r+f
            if isprime(t:=int(sn)):
                an, s = t, sn
                break
print(list(agen())) # _Michael S. Branicky_, Aug 25 2024

