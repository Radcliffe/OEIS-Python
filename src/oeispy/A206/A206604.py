# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A206604

from math import comb
def A206604(n): return sum(comb(n,k>>1)*((k<<1)-n) for k in range(n+1))+1 # _Chai Wah Wu_, Oct 28 2024

