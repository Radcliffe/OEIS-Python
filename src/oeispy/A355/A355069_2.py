# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355069

from sympy import prime
from sympy.ntheory.residue_ntheory import nthroot_mod
def A355069(n):
    p = prime(n)
    return sum(sum(len(nthroot_mod(k,y,p,True)) for y in range(1,p))**2 for k in range(p)) # _Chai Wah Wu_, Aug 31 2022

