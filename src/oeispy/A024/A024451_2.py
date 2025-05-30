# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A024451

from math import prod
from sympy import prime
def A024451(n):
    q = prod(plist:=tuple(prime(i) for i in range(1,n+1)))
    return sum(q//p for p in plist) # _Chai Wah Wu_, Nov 03 2022

