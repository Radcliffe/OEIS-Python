# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348063

from sympy.abc import x
from sympy import ff, expand
def A348063(n): return sum(ff(n,n-k)*expand(ff(x,k)).coeff(x**2) for k in range(2,n+1)) # _Chai Wah Wu_, Sep 27 2021

