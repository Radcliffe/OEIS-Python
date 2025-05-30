# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A001615

from math import prod
from sympy import primefactors
def A001615(n):
    plist = primefactors(n)
    return n*prod(p+1 for p in plist)//prod(plist) # _Chai Wah Wu_, Jun 03 2021

