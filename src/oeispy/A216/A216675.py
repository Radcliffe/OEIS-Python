# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A216675

from sympy.abc import x
from sympy import resultant, chebyshevu, I
def A216675(n): return 0 if n&1 else resultant(chebyshevu(n,x/2),chebyshevu(n,I*x/2)) # _Chai Wah Wu_, Nov 07 2023

