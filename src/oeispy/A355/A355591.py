# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355591

from itertools import count, islice
from sympy import nextprime
def agen():
    p, s, primen = 1, 0, 2
    while True:
        yield p - s; primen = nextprime(primen); p *= primen; s += primen
print(list(islice(agen(), 19))) # _Michael S. Branicky_, Jul 12 2022

