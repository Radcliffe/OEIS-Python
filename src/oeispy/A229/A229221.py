# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A229221

from sympy import isprime
def DP(n):
    p = 1
    for i in str(n):
        p *= int(i)
    return p
{print(n,end=', ') for n in range(10**3) if isprime(n-DP(n))}
## Simplified by _Derek Orr_, Apr 10 2015

