# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A282721

from sympy import isprime
def a(p):
    r=(p - 1)//2
    t=0
    for j in range(1, r + 1):
        q=(j**2)%p
        if q<=r:t+=q
    return t
print([a(p) for p in range(3, 2001, 8) if isprime(p)]) # _Indranil Ghosh_, Mar 27 2017, translated from Maple code

