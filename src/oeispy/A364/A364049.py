# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364049

from itertools import count
from sympy.ntheory import digits
def a(n): return next(k for k in count(2) if len(set(d:=digits(1<<k,n)[1:]))<len(d))
print([a(n) for n in range(2, 80)]) # _Michael S. Branicky_, Jul 05 2023

