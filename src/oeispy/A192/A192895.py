# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A192895

from sympy import divisors
def A192895(n): return sum((d.bit_count() if d<n else -d.bit_count()) for d in divisors(n,generator=True)) # _Chai Wah Wu_, Jul 25 2023

