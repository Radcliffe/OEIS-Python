# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350387

from sympy import factorint
def a(n): return sum(e for e in factorint(n).values() if e%2 == 1)
print([a(n) for n in range(1, 106)]) # _Michael S. Branicky_, Dec 28 2021

