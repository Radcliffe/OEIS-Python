# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349145

from fractions import Fraction
from itertools import product
def A349145(n): return sum(1 for d in product(range(1,n+1),repeat=n) if sum(Fraction(i+1,j) for i, j in enumerate(d)).denominator == 1) # _Chai Wah Wu_, Nov 09 2021

