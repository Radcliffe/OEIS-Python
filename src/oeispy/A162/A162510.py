# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A162510

from sympy import factorint
from operator import mul
def a(n):
    f=factorint(n)
    return 1 if n==1 else reduce(mul, [2**(f[i] - 1) for i in f]) # _Indranil Ghosh_, May 20 2017

