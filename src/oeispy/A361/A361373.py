# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A361373

from sympy import integer_log, primefactors
def A361373(n): return sum(integer_log(n,p)[0] for p in primefactors(n)) # _Chai Wah Wu_, Sep 20 2024

