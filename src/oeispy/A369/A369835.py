# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A369835

from itertools import permutations
from sympy import Matrix
def A369835(n): return len({Matrix([p[i:0:-1]+p[:n-i] for i in range(n)]).per() for p in permutations(range(n))}) # _Chai Wah Wu_, Feb 11 2024

