# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A194137

from sympy import integer_nthroot
def A194137(n): return sum(integer_nthroot(6*j**2,2)[0] for j in range(1,n+1)) # _Chai Wah Wu_, Mar 17 2021

