# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A034729

from sympy import divisors
def A034729(n): return sum(1<<(d-1) for d in divisors(n,generator=True)) # _Chai Wah Wu_, Jul 15 2022

