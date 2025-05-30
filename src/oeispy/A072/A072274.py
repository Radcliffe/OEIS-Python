# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A072274

from sympy import nextprime
from itertools import islice
def agen(): # generator of terms
    p, hp, q, hq = 2, "2", 3, "3"
    while True:
        if hp == hq: yield from [p, q]
        p, q = q, nextprime(q)
        hp, hq = hq, "".join(sorted(str(q)))
print(list(islice(agen(), 38))) # _Michael S. Branicky_, Feb 19 2024

