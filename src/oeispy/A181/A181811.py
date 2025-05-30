# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A181811

from sympy import primerange, factorint
from operator import mul
from functools import reduce
def P(n): return reduce(mul, [i for i in primerange(2, n + 1)])
def a(n):
    f = factorint(n)
    return 1 if n==1 else (reduce(mul, [P(i)**f[i] for i in f]))//n
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, May 14 2017

