# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A140757

from math import comb, isqrt
def A140757(n): return ((a-1)**2>>2)+(c>>1) if (c:=(a:=(m:=isqrt(k:=n<<1))+(k>m*(m+1)))-(b:=n-comb(a,2)))&1 else ((a+1)**2>>2)-(c>>1) # _Chai Wah Wu_, Jun 09 2025

