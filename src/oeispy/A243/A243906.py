# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A243906

from math import isqrt
from sympy import prime, primepi
def A243906(n): return int(sum(primepi(n//prime(k))-k+1 for k in range(1,primepi(isqrt(n))+1)))-primepi(n) # _Chai Wah Wu_, Jul 23 2024

