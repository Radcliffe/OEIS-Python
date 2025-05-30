# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A246353

from math import prod, isqrt
from sympy import prime, mobius
def A246353(n):
    m = prod(prime(i) for i,j in enumerate(bin(n)[-1:1:-1],1) if j=='1')
    return int(sum(mobius(k)*(m//k**2) for k in range(1, isqrt(m)+1))) # _Chai Wah Wu_, Feb 22 2025

