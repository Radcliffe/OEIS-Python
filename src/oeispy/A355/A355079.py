# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355079

from sympy import factorint
def row(n): return [1] if n < 2 else sorted(n//p for p in factorint(n))
print([an for r in range(1, 51) for an in row(r)]) # _Michael S. Branicky_, Sep 18 2022

