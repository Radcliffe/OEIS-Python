# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A293439

from sympy import factorint
def A293439(n): return sum(1 for e in factorint(n).values() if e.bit_count()&1) # _Chai Wah Wu_, Nov 23 2023

