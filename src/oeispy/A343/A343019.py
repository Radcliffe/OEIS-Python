# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A343019

from itertools import count, pairwise
from sympy import divisor_count
def A343019(n): return next(m+1 for m, t in enumerate(pairwise(map(divisor_count,count(1)))) if t[1] == t[0]-n) # _Chai Wah Wu_, Jul 25 2022

