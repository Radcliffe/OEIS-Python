# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A190867

from functools import reduce
from sympy import factorint
from operator import mul
def a(n): return 1 if n==1 else reduce(mul, [max(1, e - 1) for e in factorint(n).values()])
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Jul 19 2017

