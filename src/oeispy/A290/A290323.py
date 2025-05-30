# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A290323

from sympy import factorint
from functools import reduce
from operator import mul
def A290323(n):
    f = factorint(n)
    m = f[2] if 2 in f else 0
    a, b = divmod(m,3)
    c = 2 if m == 1 else 3**(b*(b+1)%5)*5**(a-(b%2))
    return c*reduce(mul,(((d+1)//2)**f[d] for d in f if d != 2),1) # _Chai Wah Wu_, Mar 05 2021

