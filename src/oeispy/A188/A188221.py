# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A188221

from sympy import integer_nthroot
def A188221(n): return integer_nthroot(5*(n+1)**2,2)[0]-integer_nthroot(5*n**2,2)[0]-2 # _Chai Wah Wu_, Mar 16 2021

