# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A045663

from sympy import mobius, divisors
def A045663(n): return sum(mobius(d)<<n//d for d in divisors(n>>(~n&n-1).bit_length(),generator=True)) if n else 1 # _Chai Wah Wu_, Jul 22 2024

