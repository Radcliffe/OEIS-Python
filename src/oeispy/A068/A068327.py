# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068327

from sympy import factorint
def A068327(n): return sum((n**(n+1)*e//p for p,e in factorint(n).items())) if n > 1 else 0 # _Chai Wah Wu_, Jun 12 2022

