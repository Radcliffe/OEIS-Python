# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A181812

from sympy import primerange, factorint
from operator import mul
def P(n): return reduce(mul, [i for i in primerange(2, n + 1)])
def a181811(n):
    f = factorint(n)
    return 1 if n==1 else (reduce(mul, [P(i)**f[i] for i in f]))/n
def a(n): return a181811(2*n - 1) # _Indranil Ghosh_, May 15 2017

