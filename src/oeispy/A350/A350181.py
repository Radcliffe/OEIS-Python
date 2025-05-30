# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350181

from math import prod
from sympy import factorint
def pd(n): return prod(map(int, str(n)))
def ok(n):
    if n <= 9 or max(factorint(n)) > 9: return False
    return (p := pd(n)) > 9 and pd(p) < 10
print([k for k in range(1400) if ok(k)]) # _Michael S. Branicky_, Jan 16 2022

