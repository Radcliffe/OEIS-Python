# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A125584

from math import prod
from sympy import divisor_count
from itertools import combinations
def a(n):
    R, maxd = set(range(1, n+1)), -1
    return max(divisor_count(prod(a)+prod(R-set(a))) for c in range(len(R)//2+1) for a in combinations(R, c))
print([a(n) for n in range(10)]) # _Michael S. Branicky_, Feb 09 2025

