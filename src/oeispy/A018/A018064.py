# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A018064

from sympy import integer_nthroot
def A018064(n): return -integer_nthroot(m:=7**n, 4)[0]+integer_nthroot(m<<4, 4)[0] # _Chai Wah Wu_, Jun 20 2024

