# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A341397

from math import prod
from sympy import factorint
def A341397(n): return (sum((prod((p**(3*(e+1))-(1 if p&1 else 15))//(p**3-1) for p, e in factorint(m).items()) for m in range(1,n+1)))<<4)+1 # _Chai Wah Wu_, Jun 21 2024

