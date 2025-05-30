# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349708

from math import isqrt
from sympy import primorial, divisors
def A349708(n):
    m = primorial(n+1)//2
    a = isqrt(m)
    d = max(filter(lambda d: d <= a, divisors(m,generator=True)))
    return (m//d-d)//2 # _Chai Wah Wu_, Mar 29 2022

