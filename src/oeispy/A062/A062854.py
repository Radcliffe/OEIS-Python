# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A062854

from itertools import takewhile
from sympy import divisors
def A062854(n): return sum(1 for i in range(1,n+1) if all(d<=i for d in takewhile(lambda d:d<n,divisors(n*i)))) # _Chai Wah Wu_, Oct 13 2023

