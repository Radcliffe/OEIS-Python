# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A374930

from math import prod
from sympy import factorint
def A374930(n):
    f = factorint(n).items()
    return (31*prod((p**(5*(e+1))-1)//(p**5-1) for p,e in f)-70*(n+1)*prod((p**(3*(e+1))-1)//(p**3-1) for p,e in f) + (20*n*((n<<1)+3)+9)*prod((p**(e+1)-1)//(p-1) for p, e in f))//1920 # _Chai Wah Wu_, Jul 24 2024

