# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350955

from itertools import permutations
from sympy import Matrix, prime
def A350955(n): return min(Matrix([p[i:0:-1]+p[0:n-i] for i in range(n)]).det() for p in permutations(prime(i) for i in range(1,n+1))) # _Chai Wah Wu_, Jan 27 2022

