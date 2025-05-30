# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A152597

from itertools import islice
from sympy import nextprime, n_order
def agen():
    record, v, p = -1, 1, 3
    while True:
        if v > record: record = v; yield record
        v, p = (p-1)//n_order(2, p), nextprime(p)
print(list(islice(agen(), 20))) # _Michael S. Branicky_, Oct 09 2022

