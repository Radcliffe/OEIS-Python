# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A050689

from sympy import factorint
def ok(n): return 1 < sum(map(int, str(n))) == sum(factorint(n).values())
print([k for k in range(11000) if ok(k)]) # _Michael S. Branicky_, Dec 30 2021

