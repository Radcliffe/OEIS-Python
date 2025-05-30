# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353691

from math import prod, gcd
from sympy import factorint
def A353691_helper(n):
    f = factorint(n).items()
    return prod(p**e*(p-1)*(e+1) for p, e in f), prod(p**(e+1)-1 for p, e in f)
def A353691(n):
    Hnp, Hnq = A353691_helper(n)
    g = gcd(Hnp, Hnq)
    Hnp //= g
    Hnq //= g
    k = n+1
    Hkp, Hkq = A353691_helper(k)
    while (Hkp*Hnq) % (Hkq*Hnp):
        k += 1
        Hkp, Hkq = A353691_helper(k)
    return k # _Chai Wah Wu_, May 07 2022

