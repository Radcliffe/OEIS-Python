# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A381020

from math import isqrt
from sympy import isprime
def A381020(n): return sum(1 for m in range(1,100*n+1) if isprime(1+(sum(isqrt(k*((m<<1)-k)) for k in range(1,m+1))<<2))) # _Chai Wah Wu_, Feb 13 2025

