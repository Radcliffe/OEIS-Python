# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A078433

from itertools import permutations
from sympy import isprime
from sympy.ntheory.continued_fraction import continued_fraction_reduce
def A078433(n): return sum(1 for p in permutations(range(1,n+1)) if isprime(continued_fraction_reduce(p).p)) # _Chai Wah Wu_, Sep 22 2021

