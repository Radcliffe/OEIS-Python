# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A067538

# uses A008284_T
from sympy import divisors
def A067538(n): return sum(A008284_T(n,d) for d in divisors(n,generator=True)) # _Chai Wah Wu_, Sep 21 2023

