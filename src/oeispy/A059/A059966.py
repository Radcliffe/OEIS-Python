# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A059966

from sympy import mobius, divisors
def A059966(n): return sum(mobius(n//d)*(2**d-1) for d in divisors(n,generator=True))//n # _Chai Wah Wu_, Feb 03 2022

