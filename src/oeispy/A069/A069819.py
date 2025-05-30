# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A069819

from sympy import factorint
from fractions import Fraction
def ok(n):
    s = sum(Fraction(1, p) for p in factorint(n))
    return s > 1 and (s - 1).numerator == 1
print([k for k in range(1, 4501) if ok(k)]) # _Michael S. Branicky_, Dec 19 2021

