# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A076634

from sympy import prod, Poly
from sympy.abc import x
def A076634(n):
    y = Poly(prod(2*x+i for i in range(1,n+1))).all_coeffs()[::-1]
    return y.index(max(y)) # _Chai Wah Wu_, Mar 07 2021

