# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A190619

from math import isqrt, comb
def A190619(n): return (10**((a:=(isqrt(n<<3)+1>>1)+1)+1)-1)//9-10**(comb(a,2)-n+1) # _Chai Wah Wu_, Dec 18 2024

