# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A128227

from math import comb, isqrt
def A128227(n): return n-comb(r:=(m:=isqrt(k:=n+1<<1))+(k>m*(m+1))+1,2)+(2 if k==m*(m+1) else r) # _Chai Wah Wu_, Nov 09 2024

