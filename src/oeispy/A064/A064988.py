# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A064988

from sympy import factorint, prime
from operator import mul
def a(n): return 1 if n==1 else reduce(mul, [prime(p)**e for p, e in factorint(n).items()])
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Aug 08 2017

