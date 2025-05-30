# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A320940

from sympy import divisor_sigma, divisors
def A320940(n):
    return sum(divisor_sigma(d)*(n//d)**(n+1) for d in divisors(n,generator=True)) # _Chai Wah Wu_, Feb 15 2020

