# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A361199

from sympy import isprime
from itertools import islice
def agen(): # generator of terms
    an, sums = 2, [1]
    yield 1
    while True:
        yield an
        sums = [s + an for s in sums] + [an]
        an = sum(1 for s in sums if isprime(s))
print(list(islice(agen(), 80))) # _Michael S. Branicky_, Mar 22 2023

