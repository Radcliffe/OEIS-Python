# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A038475

from math import isqrt, comb
from sympy import integer_nthroot
def A038475(n): return 5**((r:=n-1-comb((m:=integer_nthroot(6*n,3)[0])+(t:=(n>comb(m+2,3)))+1,3))-comb((k:=isqrt(b:=r+1<<1))+(b>k*(k+1)),2))+5**((a:=isqrt(s:=n-comb(m-(t^1)+2,3)<<1))+((s<<2)>(a<<2)*(a+1)+1))+5**(m+t+1) # _Chai Wah Wu_, Apr 04 2025

