# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376254

from math import prod
from sympy import factorint
def ok(n): return prod(int(str(p)+str(e)) for p, e in factorint(n).items()) < n
print([k for k in range(1, 3200) if ok(k)]) # _Michael S. Branicky_, Sep 27 2024

