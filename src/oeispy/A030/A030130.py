# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A030130

from math import isqrt, comb
def A030130(n): return (1<<(a:=(isqrt(n-1<<3)+1>>1)+1))-(1<<comb(a,2)-n+1)-1 # _Chai Wah Wu_, Dec 19 2024

