# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A363590

from sympy import divisors
def A363590(n): return sum(d**d for d in divisors(n>>(~n & n-1).bit_length(),generator=True)) # _Chai Wah Wu_, Jul 09 2023

