# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A085239

from sympy import integer_log
def A085239(n): return 1 if n==1 else 2 if 6**integer_log(m:=3**(n-1),6)[0]<<1<m else 3 # _Chai Wah Wu_, Feb 04 2025

