# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342034

from math import prod
from itertools import combinations_with_replacement as cwr
def c(digs): return int("".join(map(str, digs))) < prod(digs) * sum(digs)
def a(n): return sum(1 for u in cwr(range(1, 10), n) if c(u))
print([a(n) for n in range(1, 16)]) # _Michael S. Branicky_, Mar 05 2021

