# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A341885

from sympy import factorint
def A341885(n): return sum(k*m*(m+1)//2 for m,k in factorint(n).items()) # _Chai Wah Wu_, Feb 25 2021

