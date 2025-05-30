# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A114429

from sympy import prevprime
def a(n):
    p = prevprime(10**n); pp = prevprime(p)
    while p - pp != 2: p, pp = pp, prevprime(pp)
    return p
print([a(n) for n in range(1, 19)]) # _Michael S. Branicky_, Jan 17 2022

