# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A061885

from math import comb, isqrt
def A061885(n): return n+comb((m:=isqrt(k:=n+1<<1))+(k>m*(m+1)),2) # _Chai Wah Wu_, Nov 09 2024

