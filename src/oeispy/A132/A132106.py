# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A132106

from math import isqrt
def A132106(n): return (lambda m: 2*(sum(n//k for k in range(1, m+1)))+m*(1-m)+1)(isqrt(n)) # _Chai Wah Wu_, Oct 08 2021

