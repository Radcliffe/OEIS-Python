# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377487

from sympy import integer_log, primefactors
def A377487(n): return max((p**integer_log(n,p)[0] for p in primefactors(n)), default=1) # _Chai Wah Wu_, Nov 01 2024

