# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357671

from math import comb
def A357671(n): return comb(n<<1,n)+sum(comb(n+k-1,k)**2 for k in range(n+1)) if n else 2 # _Chai Wah Wu_, Oct 28 2022

