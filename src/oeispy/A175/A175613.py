# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A175613

from math import isqrt
from sympy import prime, primepi
def A175613(n):
    m = 1<<prime(n)
    return int(sum(primepi(m//prime(k))-k+1 for k in range(1,primepi(isqrt(m))+1))) # _Chai Wah Wu_, Jul 23 2024

