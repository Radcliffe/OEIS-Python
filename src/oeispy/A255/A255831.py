# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A255831

from sympy import resultant
from sympy.abc import x
def A255831_T(m,n): return resultant(x**m+n,(x+1)**m+n) # _Chai Wah Wu_, May 08 2024

