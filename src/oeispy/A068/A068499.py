# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068499

from sympy import prime
def A068499(n): return prime(n-1)-1 if n>3 else n # _Chai Wah Wu_, Aug 27 2024

