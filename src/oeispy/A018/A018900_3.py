# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A018900

from math import isqrt, comb
def A018900(n): return (1<<(m:=isqrt(n<<3)+1>>1))+(1<<(n-1-comb(m,2))) # _Chai Wah Wu_, Oct 30 2024

