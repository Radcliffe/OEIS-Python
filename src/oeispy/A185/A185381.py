# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A185381

from math import isqrt
from sympy import fibonacci
def A185381(n): return fibonacci((n+isqrt(5*n**2))//2) # _Chai Wah Wu_, Jan 11 2022

