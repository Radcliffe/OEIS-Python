# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A033942

from sympy import factorint
def ok(n): return sum(factorint(n).values()) > 2
print([k for k in range(145) if ok(k)]) # _Michael S. Branicky_, Sep 10 2022

