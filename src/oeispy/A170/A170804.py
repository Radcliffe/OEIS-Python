# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A170804

from sympy import integer_log
def A170804(n): return 1 if n == 1 else ((a:=1<<k+1)<<1)-1+(3**integer_log(a,3)[0]*3-1>>1) if 6**(k:=integer_log(m:=3**(n-2),6)[0])<<1<m else ((a:=3**integer_log(1<<n-1,6)[0])*3-1>>1)+(1<<a.bit_length())-1 # _Chai Wah Wu_, Feb 05 2025

