# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350566

from itertools import permutations
from sympy import Matrix
def A350566(n): return 1 if n == 0 else max(Matrix(n,n,p).per() for p in permutations(range(1,n**2+1))) # _Chai Wah Wu_, Jan 21 2022

