# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A336957

from math import gcd
from sympy import factorint
from itertools import count, islice
def agen(): # generator of terms
    a, seen, minan = [1, 2], {1, 2}, 3
    yield from a
    for n in count(3):
        an, fset = minan, set(factorint(a[-1]))
        while True:
            if an not in seen and gcd(an, a[-1])>1 and gcd(an, a[-2])==1:
                if set(factorint(an)) - fset > set():
                    break
            an += 1
        a.append(an); seen.add(an); yield an
        while minan in seen: minan += 1
print(list(islice(agen(), 70))) # _Michael S. Branicky_, Jan 22 2022

