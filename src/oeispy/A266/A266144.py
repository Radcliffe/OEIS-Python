# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A266144

from __future__ import division
from sympy import isprime
def A266144(n):
    return 4 if n==1 else sum(1 for d in [-4,-2,2,4] if isprime(5*(10**n-1)//9+d)) # _Chai Wah Wu_, Dec 27 2015

