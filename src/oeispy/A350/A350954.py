# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350954

from itertools import permutations
from sympy import Matrix
def A350954(n): return max(Matrix([p[i:0:-1]+p[0:n-i] for i in range(n)]).det() for p in permutations(range(1,n+1))) # _Chai Wah Wu_, Jan 27 2022

